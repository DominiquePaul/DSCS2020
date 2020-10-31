"""
___ Hashing Passwords ___

So far we've been storing passwords as plain text. This is generally a bad
idea, because if anybody every gets access to your database then they can see
the passwords of your functions. What we will now do is "hash" the passwords
entered. Hashing is a bit like encryption: we convert the pure text into a
combination of characters and numbers that are not understandable.

Its very easy to convert a string to a hash, but its very hard to understand
what the origial string was when you just know the hash.

We will use the bcrypt package that helps us generate and validate secure
hashes for passwords

We need to do three things to use encrypted passwords:
    1. Initialise the bcrypt object
    2. Change our registration functions
    3. Change our login validation function

You might need to run this line to install the bcrypt package first:

    pip install flask-bcrypt

"""

import pandas as pd
import datetime

from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# new line
from flask_bcrypt import Bcrypt

from forms import RegistrationForm, LoginForm, PostForm


app = Flask(__name__)

# 1. Initialise the bcrypt object
# we create a bcrypt object in our flask app that we will use to create and
# validate hashes
bcrypt = Bcrypt(app)

app.config["SECRET_KEY"] = "enter-a-hard-to-guess-string"

###############################################################################
# Database configuration
###############################################################################

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


class User(db.Model):
    # primary key is the unique identifier for each row
    id = db.Column(db.Integer, primary_key=True)
    # nullable means that the value cannot be empty
    name = db.Column(db.String(60), nullable=False)
    # unique ensures that values already in this column cannot be entered again
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    products = db.relationship("Products", backref="vendor", lazy=True)

    def __repr__(self):
        """
        This is the string that is printed out if we call the print function
            on an instance of this object
        """
        return f"User(id: '{self.id}', name: '{self.name}', " +\
               f" email: '{self.email}')"


class Products(db.Model):
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
    form = RegistrationForm()

    if form.validate_on_submit():
        registration_worked = register_user(form)
        if registration_worked:
            return redirect(url_for("login"))

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if is_login_successful(form):
            return redirect(url_for("upload"))
        else:
            return redirect(url_for("register"))

    return render_template("login.html", form=form)


@app.route("/upload", methods=["GET", "POST"])
def upload():
    form = PostForm()

    if form.validate_on_submit():
        add_product(form)
        return redirect(url_for("index"))

    return render_template("upload.html", form=form)


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
        return False

    # 2. We change the registration form to hash passwords
    hashed_password = bcrypt.generate_password_hash(form_data.password.data)

    user = User(name=form_data.name.data,
                email=form_data.email.data,
                password=hashed_password)  # changed this line

    db.session.add(user)

    db.session.commit()

    return True


def is_login_successful(form_data):

    email = form_data.email.data
    password = form_data.password.data

    user = User.query.filter_by(email=email).first()

    if user is not None:
        if bcrypt.check_password_hash(user.password, password):
            return True

    return False


def add_product(form_data):

    product = Products(name=form_data.item_name.data,
                       description=form_data.description.data,
                       price=form_data.price.data,
                       user_id=1)  # we set 1 as a default here for now

    db.session.add(product)

    db.session.commit()


def get_products():
    df = pd.read_sql(Products.query.statement, db.session.bind)

    return df


if __name__ == "__main__":
    app.run(debug=True)
