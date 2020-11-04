
import os
from flask import Flask, render_template, redirect, url_for

from wtforms import SubmitField
from wtforms.validators import DataRequired

from flask_wtf import Form
from flask_wtf.file import FileField

app = Flask(__name__)
app.config["SECRET_KEY"] = "enter-a-hard-to-guess-string"


class FileUpload(Form):
    user_file = FileField("Your Data", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/', methods=['GET', 'POST'])
def index():

    form = FileUpload()

    if form.validate_on_submit():

        # read the file content
        assets_dir = "static/assets"

        d = form.user_file.data

        filename = d.filename

        d.save(os.path.join(assets_dir, filename))



        return redirect(url_for("show_image", filename=filename))

    return render_template("index.html", form=form)


@app.route('/image/<filename>')
def show_image(filename):

    file_path_in_static = os.path.join("assets", filename)

    return render_template("show_image.html", img_name=file_path_in_static)


if __name__ == "__main__":
    app.run(debug=True)
