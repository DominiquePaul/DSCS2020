"""
___ Adding user session management ___

When users successfully login we want to save that status as "logged in" for
our application, so that we are able to access the status (logged in or not) as
well as information about the user.

For this we can use another extension of flask called flask-login which takes
care about all of this for us. The way that this works is that we add some
functionality to the sql table modules and the flask login manager takes care
of most other issues for us

Link to the docs:
https://flask-login.readthedocs.io/en/latest/


You might need to run this line to install the flask-login package first:

    pip install flask-login

We need to do 7 things to add session management
    1. Initialise the login manager
    2. Define a user_loader helper function for the login manager
    3. Adjust our table classes
    4. Adjust our login function
    5. Prettify our app to consider logged-in / logged out states
        a. Create redirects if a logged in user wants to access the login or
            register page
        b. Use jinja to change the html navbar to either show "login" and
            "register" when the user is not logged in yet and show display
            "logout" when logged in (not applicable in our app, because we
            have no pretty navbar in our app)
    6. Create a logout link
    7. Optionally restrict access to some pages for non logged in users. For
        this we have to:

        a. Define where users should be redirect to when they try to access a
            route with restricted viewing conditions (ideally they should be
            redirected to the login route)
        b. Use the decorator @login_required to specify the pages with
            restrictions

"""

import pandas as pd
import datetime

from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# new import line
from flask_login import LoginManager, UserMixin, login_user, current_user
from flask_login import logout_user, login_required

from forms import RegistrationForm, LoginForm, PostForm


app = Flask(__name__)

app.config["SECRET_KEY"] = "enter-a-hard-to-guess-string"

bcrypt = Bcrypt(app)
# 1. Initialise the login manager, this is a common pattern for flask
#   extensions to inherit the information from the main flask app
login_manager = LoginManager(app)

# 7. Optionally restrict access to some pages for non logged in users
# a. Define where users should be redirect to when they try to access a
#    route with restricted viewing conditions (ideally they should be
#    redirected to the login route)
#
# This is kind of like the content that you would place in
# redirect(url_for(...))
# We might be using the "login_required" decorator (indicated by @) multiple
# times and wouldnt want to specify the same redirect url all the time
login_manager.login_view = "login"


###############################################################################
# Database configuration
###############################################################################

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


# 2. Define a user_loader helper function for the login manager
# this is copied and adjusted from the documenation (link above)
#
# This is a function that we have to define for the login manager to know how
# it can get information on a user when it has the users id. We are basically
# using what we learnt about querying from the last part
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# 3. Adjust our table classes
# As we can see in the documentation, the login manager expects our classes to
# have certain methods implemented, that it can access. These are called
# is_authenticated, is_active, is_anonymous, get_id
#
# we could define these ourself, but reading the documentation carefully we can
# also just make our objects inherit from the Mixin object as follows below.
# If interested you can also see how you could define these functions yourself
# here:
# https://realpython.com/using-flask-login-for-user-management-with-flask/
class User(db.Model, UserMixin):
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

    # 5. Prettify our app to consider logged-in / logged out states
    # we can use the imported object "current_user" to know if the person
    # viewing the page is logged in and get basic information about that user
    #
    # As it wouldn't make sense to register or login again if you already are
    # logged in we don't want the logged in user to access this page in the
    # first place. We add this to the register and login route.
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = RegistrationForm()

    if form.validate_on_submit():
        registration_worked = register_user(form)
        if registration_worked:
            return redirect(url_for("login"))

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():

    # 5. Prettify our app to consider logged-in / logged out states
    # we can use the imported object "current_user" to know if the person
    # viewing the page is logged in and get basic information about that user
    #
    # As it wouldn't make sense to register or login again if you already are
    # logged in we don't want the logged in user to access this page in the
    # first place. We add this to the register and login route.
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = LoginForm()

    if form.validate_on_submit():
        if is_login_successful(form):
            return redirect(url_for("upload"))
        else:
            return redirect(url_for("register"))

    return render_template("login.html", form=form)


# 7. Optionally restrict access to some pages for non logged in users.
# b. Use the decorator @login_required to specify the pages with
#    restrictions
#
# We just need to add this decorator with an @ in front of any page that the
# user needs to login
@app.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    form = PostForm()

    if form.validate_on_submit():
        add_product(form)
        return redirect(url_for("index"))

    return render_template("upload.html", form=form)


# 6. Create a logout link
@app.route("/logout")
def logout():
    # we dont need any arguments here, the login package already knows who the
    # current user is
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
        return False

    # 2. We change the registration form to hash passwords
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

            # 4. Adjust our login function
            #
            # we pass our user object that we retrieved from the database
            # to the login manager, so it knows which user signed in to the
            # current browser session
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
