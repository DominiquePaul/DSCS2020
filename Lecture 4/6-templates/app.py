# Templates are a nice and easy to show prettier content to users using html
# You have to place your .html files in a folder called "templates" and then
# use the 'render_template' function to return them

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("my_template.html")


if __name__ == "__main__":
    app.run(debug=True)
