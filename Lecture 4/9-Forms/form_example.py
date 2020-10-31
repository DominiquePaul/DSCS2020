# you might have to install the following packages
# pip install email_validator
# pip install Flask-WTF


from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)

# The flask form package expects a so-called secret key that it can use for
# encryption to ensure a decent level of security (e.g. for passwords)
app.config["SECRET_KEY"] = "enter-a-hard-to-guess-string"


# you might have to install the package 'flask-wtf'
class MyForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/", methods=["GET", "POST"])
def index():
    form = MyForm()
    name = "no input"
    age = 0

    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data

    return render_template("3-form_example.html",
                           form=form,
                           name=name,
                           age=age)


if __name__ == "__main__":
    app.run(debug=True)
