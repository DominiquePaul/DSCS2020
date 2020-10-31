# Forms are a great way of making apps interactive for users. One easy eay
# of building forms in by using the flask wt forms package
# https://flask-wtf.readthedocs.io/en/stable/

# you might have to install the following
# pip install WTForms
# pip install email_validator

from flask import Flask, render_template, redirect

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email

import datetime

app = Flask(__name__)

# The flask form package expects a so-called secret key that it can use for
# encryption to ensure a decent level of security (e.g. for passwords)
app.confnig["SECRET_KEY"] = "enter-a-hard-to-guess-string"


bar_employees = ["Martha", "Lisa", "Alan"]
bar_products = {"Schützengarten": 4.50,
                "Klosterbräu": 4.50,
                "White Wine": 8.5,
                "Red Wine": 8.5,
                "Moscow Mule": 12.0,
                "Gin Tonic": 13.0
                }


@app.route("/")
def index():

    hour_of_day = datetime.datetime.now().hour

    return render_template("1-basic.html",
                           company="Ad Hoc",
                           employees=bar_employees,
                           products=bar_products,
                           hour_of_day=hour_of_day)


# forms
#
# you might have to install the package 'flask-wtf'
class ContactForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired()])

    email = StringField("Email",
                        validators=[DataRequired(), Email()])

    hour = IntegerField("After which full hour did you arrive?",
                        validators=[DataRequired()])

    submit = SubmitField("Submit")


# Adding POST to the list of methods is necessary because form submissions are
# generally treated as post requests
@app.route("/contact-tracing", methods=["GET", "POST"])
def contact_form():



    hour_of_day = datetime.datetime.now().hour
    form = ContactForm()

    # the validate_on_submit function returns True if the form is submitted and
    # the data was accepted by all validators. We use it to decide whether we
    # want to render the form or process the results
    if form.validate_on_submit():



        return redirect("http://0.0.0.0:5000/")
    else:
        return render_template("2-contact_form.html",
                               company="Ad Hoc",
                               employees=bar_employees,
                               products=bar_products,
                               hour_of_day=hour_of_day,
                               form=form)


if __name__ == "__main__":
    app.run(debug=True)
