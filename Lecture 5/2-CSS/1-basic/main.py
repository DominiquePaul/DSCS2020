"""
What does CSS do?

    * Style your html files

    * Order elements in your html file

---

One HTML file, 5 CSS files = 5 different websites:
https://www.w3schools.com/css/css_intro.asp

---

There are three ways of adding css styles to a html file

    1. Inline - by using the style attribute inside HTML elements like this:
        <p style="color: green;"> text goes there </p>

    2. Internal - by using a <style> element in the <head> section

    3. External - by using a <link> element to link to an external CSS file

---

A general hint when making many html/css changes during development:

Sometimes html and css is cached (saved locally by your browser). Due to this
you won't always see refreshes when reloading the page. You can make sure that
this isn't happening by either

    (a) Refreshing without cache command/ctrl + shift + r

    (b) Working in the incognito mode of your browser (doesn't cache data)

"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("0-index.html")


@app.route("/inline")
def inline():
    return render_template("1-inline.html")


@app.route("/internal")
def internal():
    return render_template("2-internal.html")


@app.route("/external")
def external():
    return render_template("3-external.html")


if __name__ == "__main__":
    app.run(debug=True)
