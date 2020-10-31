from flask import Flask, render_template

# initialisation
app = Flask(__name__)


# first webaddress. '/' stands for home
@app.route("/")
def index():
    return "Hello world!"


@app.route("/html-basics")
def html_basics():
    return render_template("1-basics.html")


@app.route("/general-format")
def general_format():
    return render_template("2-file_structure.html")


if __name__ == "__main__":
    app.run()
