
import os
import sys
import pandas as pd
import datetime

from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# new import line
from flask_login import LoginManager, UserMixin, login_user, current_user
from flask_login import logout_user, login_required

from forms import RegistrationForm, LoginForm, PostForm

# this file is missing because it is included in the gitignore. You have to
# create your own and fill it with the following variables
from secrets import SQL_PASSWORD, SQL_PUBLIC_IP, SQL_DATABASE_NAME

from google.cloud import storage
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./gcp_credentials/dscs2020-b20a630b58a2.json"


app = Flask(__name__)

###############################################################################
# Google Cloud Storage settings
GC_BUCKET_NAME = "ascet-fashion-showroom"

# Google Cloud SQL settings
PASSWORD = SQL_PASSWORD
PUBLIC_IP_ADDRESS = SQL_PUBLIC_IP
DBNAME = SQL_DATABASE_NAME

# configuration
app.config["SECRET_KEY"] = "A2BD87117A791E89"
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://postgres:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True


###############################################################################

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)

login_manager.login_view = "login"


###############################################################################
# Database configuration
###############################################################################


db = SQLAlchemy(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    # We change the column type from string to binary for the password field.
    # This is something we could have also done earlier with SQLite, but we got
    # away without it. Now we have to channge it as the encrypted password is
    # a binary string which causes errors due to the datatype change by SQL
    # Alchemy and PostgreSQL
    password = db.Column(db.Binary(100), nullable=False)
    products = db.relationship("Products", backref="vendor", lazy=True)

    def __repr__(self):
        """
        This is the string that is printed out if we call the print function
            on an instance of this object
        """
        return f"User(id: '{self.id}', name: '{self.name}', " +\
               f" email: '{self.email}')"


class Products(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    # we can set default values manually or by adding a function (without
    # brackets because otherwise we would be calling it)
    date_created = db.Column(db.DateTime, nullable=False,
                             default=datetime.datetime.now)
    img_public_url = db.Column(db.String, nullable=False)
    img_gcs_path = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        """
        This is the string that is printed out if we call the print function
            on an instance of this object
        """
        return f"Product(id: '{self.id}', name: '{self.name}', description:" +\
               f" '{self.description}', price: '{self.price}', date_created" +\
               f": '{self.date_created}', public_url: '{self.img_public_url}'" +\
               f"gcs_path: '{self.img_gcs_path}', vendor: '{self.user_id}')"


###############################################################################
# Routes
###############################################################################


@app.route("/")
def index():
    products = get_products()
    return render_template("index.html", products_df=products)


@app.route("/register", methods=["GET", "POST"])
def register():

    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = RegistrationForm()

    if form.validate_on_submit():
        registration_worked = register_user(form)
        if registration_worked:
            flash("Registration successful")
            return redirect(url_for("login"))

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = LoginForm()

    if form.validate_on_submit():
        if is_login_successful(form):
            flash("Login successful")
            return redirect(url_for("upload"))
        else:
            flash("Login unsuccessful, please check your credentials and try again")
            return redirect(url_for("register"))

    return render_template("login.html", form=form)


@app.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    form = PostForm()

    if form.validate_on_submit():
        flash("Product uploaded successfully")
        add_product(form)
        return redirect(url_for("index"))

    return render_template("upload.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


###############################################################################
# Helper functions
###############################################################################

def register_user(form_data):

    def email_already_taken(email):
        if User.query.filter_by(email=email).count() > 0:
            return True
        else:
            return False

    if email_already_taken(form_data.email.data):
        flash("That email is already taken!")
        return False

    hashed_password = bcrypt.generate_password_hash(form_data.password.data)

    user = User(name=form_data.name.data,
                email=form_data.email.data,
                password=hashed_password)

    db.session.add(user)

    db.session.commit()

    return True


def is_login_successful(form_data):

    email = form_data.email.data
    password = form_data.password.data

    user = User.query.filter_by(email=email).first()

    if user is not None:
        if bcrypt.check_password_hash(user.password, password):

            login_user(user)

            return True

    return False


def add_product(form_data):

    image_as_bytes = form_data.image_upload.data.read()
    print(type(image_as_bytes), file=sys.stderr)
    file_name = form_data.item_name.data

    public_url = upload_bytes_to_gcs(bucket_name=GC_BUCKET_NAME,
                                     bytes_data=image_as_bytes,
                                     destination_blob_name=file_name)

    product = Products(name=form_data.item_name.data,
                       description=form_data.description.data,
                       price=form_data.price.data,
                       user_id=current_user.id,
                       img_public_url=public_url,
                       img_gcs_path=file_name)

    db.session.add(product)

    db.session.commit()


def get_products():

    df = pd.read_sql(Products.query.statement, db.session.bind)

    return df


def upload_bytes_to_gcs(bucket_name, bytes_data, destination_blob_name):

    storage_client = storage.Client()

    # get the bucket by name
    bucket = storage_client.bucket(bucket_name)

    # this creates the blob object in python but does not upload anything
    blob = bucket.blob(destination_blob_name)

    # upload the file
    blob.upload_from_string(bytes_data)

    # set the image to be publicly viewable
    blob.make_public()

    # get publicly viewable image of url
    public_img_url = blob.public_url

    return public_img_url


if __name__ == "__main__":
    app.run(debug=True)
