from flask import Flask, render_template

"""

__ About Bootstrap __
Bootstrap is a framework to build simple yet good looking html websites
with little effort. They provide basic styles, icons, and entire website
themes.

https://getbootstrap.com/

---

__ Note __
There are different ways to implement bootstrap with flask. Either by package
or by referencing the stylesheets in the html. Either way works, yet as the
main bootstrap package for flask is only compatible with Bootstrap 3 (current
version is 4), we will cover the method that references the stylesheets.
"""

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("1-no_bootstrap.html")


@app.route("/bootstrap_v1")
def bootstrap_v1():
    return render_template("2-bootstrap_v1.html")


@app.route("/bootstrap_v2")
def bootstrap_v2():
    return render_template("3-bootstrap_v2.html")


@app.route("/bootstrap_v3")
def bootstrap_v3():
    return render_template("4-bootstrap_v3.html")


@app.route("/bootstrap_v4")
def bootstrap_v4():
    return render_template("5-bootstrap_v4.html")


if __name__ == "__main__":
    app.run(debug=True)
