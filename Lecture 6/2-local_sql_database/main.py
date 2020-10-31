"""
___ Working with databases ___

In this part we will replace our local csv database with a proper SQL database
which we will be interacting with using SQL Alchemy, a popular object
relational mapper (ORM) which basically just means that sql tables are
represented as objects in Python.

The nice thing about thiis that we can easily exchange the database running in
the background, whenever we want without having to change the code. We can work
with a local database here and use a cloud based database later just by
exchanging the link

You might need to run this first in your terminal to install flask-sqlalchemy

    pip install flask-sqlalchemy


The things we need to do to use a database:

    1. Specify a path for the database (this can also be a local path)
    2. initialise the db object
    3. Define our tables that we want to use
    4. Initialise our database using `db.create_all()`. This is not done in the
        flask app file itself, but in a separete one, here this is
        sqlalchemy_commands.py
    5. Adjust our helper functions for storing and retrieving data
"""


import pandas as pd
import datetime
from flask import Flask, render_template, redirect, url_for
# we import the flask_sqlalchemy package
from flask_sqlalchemy import SQLAlchemy

from forms import RegistrationForm, LoginForm, PostForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "enter-a-hard-to-guess-string"

###############################################################################
# Database configuration
###############################################################################

# 1. Specify a path for the database (this can also be a local path)
# We need to specify the location of the database (DB) first. We don't have a
# DB yes, so we will just reference the local directory and flask-sqlalchemy
# will create a SQLlite database for us.
#
# SQLlite is very simple type of SQL database, other types you might have heard
# of before is mySQL or postgreSQL
#
# The three slashes in the file path indicate that the path after the slashes
# is a relative path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# 2. initialise the db object
# we create the database instance. This is the object in our code representing
# the Database
db = SQLAlchemy(app)


# 3. Define our tables that we want to use
# We now define the tables that we want in our database, each table is
# represented as a class
class User(db.Model):
    # primary key is the unique identifier for each row
    id = db.Column(db.Integer, primary_key=True)
    # nullable means that the value cannot be empty
    name = db.Column(db.String(60), nullable=False)
    # unique ensures that values already in this column cannot be entered again
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    # the class user and products have a relationship: each product was posted
    # by a specific user and we actually want to display that. One product can
    # have one vendor (user) but one user (vendor) can have multiple products,
    # this is what you call a one-to-many relationship in SQL in IT language
    # We can represet this as follows in our database:
    products = db.relationship("Products", backref="vendor", lazy=True)
    # backref: we can check on the posts of the user by using the "vendor"
    #   attribute as if it were a column (see separate script)
    # lazy: the data from the products table is loaded only when we request it,
    #   not in advance

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
    id_of_user = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

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
    single_product = Products.query.first()
    return render_template("index.html",
                           products_df=products,
                           single_product=single_product)


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

# 5. Adjust our helper functions for storing and retrieving data

def register_user(form_data):

    def email_already_taken(email):
        if User.query.filter_by(email=email).count() > 0:
            return True
        else:
            return False

    if email_already_taken(form_data.email.data):
        return False

    user = User(name=form_data.name.data,
                email=form_data.email.data,
                password=form_data.password.data)

    db.session.add(user)

    db.session.commit()

    return True


def is_login_successful(form_data):

    email = form_data.email.data
    password = form_data.password.data

    are_credentials_correct = User.query.filter_by(email=email,
                                                   password=password)\
                                  .count()

    return are_credentials_correct


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
