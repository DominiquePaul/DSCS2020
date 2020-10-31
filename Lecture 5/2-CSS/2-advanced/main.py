from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("version1.html")


@app.route("/version2")
def version2():
    return render_template("version2.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
