import pandas as pd
from flask import Flask, render_template, redirect, url_for

from forms import RegistrationForm, LoginForm, PostForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "enter-a-hard-to-guess-string"

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
    user_data = pd.read_csv("data/user_data.csv")

    if form_data.email.data in user_data["email"]:
        return False

    user_data = user_data.append({"name": form_data.name.data,
                                  "email": form_data.email.data,
                                  "password": form_data.password.data},
                                 ignore_index=True)

    user_data.to_csv("data/user_data.csv", index=False)

    return True


def is_login_successful(form_data):

    user_data = pd.read_csv("data/user_data.csv")

    email = form_data.email.data
    password = form_data.password.data

    is_email_in_database = email in list(user_data["email"])

    if is_email_in_database:

        passwords_bool_mask = user_data.loc[user_data["email"] == email,
                                            "password"] == password
        is_password_correct = passwords_bool_mask.any()

        if is_password_correct:
            return True

    return False


def add_product(form_data):
    post_data = pd.read_csv("data/product_data.csv")

    post_data = post_data.append({"name": form_data.item_name.data,
                                  "description": form_data.description.data,
                                  "price": form_data.price.data},
                                 ignore_index=True)

    post_data.to_csv("data/product_data.csv", index=False)


def get_products():
    post_data = pd.read_csv("data/product_data.csv")

    return post_data


if __name__ == "__main__":
    app.run(debug=True)
