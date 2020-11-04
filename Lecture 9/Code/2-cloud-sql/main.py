
import pandas as pd
import datetime

from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# new import line
from flask_login import LoginManager, UserMixin, login_user, current_user
from flask_login import logout_user, login_required

from forms import RegistrationForm, LoginForm, PostForm

# changes to work with cloud sql
from google.cloud import storage
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../gcp_credentials/dscs2020-b20a630b58a2.json"

from secrets import SQL_PASSWORD, SQL_PUBLIC_IP, SQL_DATABASE_NAME

app = Flask(__name__)

###############################################################################
# Google Cloud SQL settings
PASSWORD = SQL_PASSWORD
PUBLIC_IP_ADDRESS = SQL_PUBLIC_IP
DBNAME = SQL_DATABASE_NAME

# configuration
app.config["SECRET_KEY"] = "A2BD87117A791E89"
#  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # --> old connection string
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
    # away without it. Now we have to change it as the encrypted password is
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
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        """
        This is the string that is printed out if we call the print function
            on an instance of this object
        """
        return f"Product(id: '{self.id}', name: '{self.name}', description:" +\
               f" '{self.description}', price: '{self.price}', date_created" +\
               f": '{self.date_created}', vendor: '{self.user_id}')"


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

    product = Products(name=form_data.item_name.data,
                       description=form_data.description.data,
                       price=form_data.price.data,
                       user_id=current_user.id)

    db.session.add(product)

    db.session.commit()


def get_products():
    df = pd.read_sql(Products.query.statement, db.session.bind)

    return df


if __name__ == "__main__":
    app.run(debug=True)
