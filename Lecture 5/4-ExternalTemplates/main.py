"""

----------------------------------
__ Tips for adjusting templates __
----------------------------------

Steps to reconfigure another template for your purposes:

    0. Open the file locally in the folder that you downloaded it in (double
        click it) to check that everything downloaded correctly

    1. Copy the index file (or multiple html files) into your templates folder

    2. Copy all other files into the static folder

    3. Adjust the html file(s): turn all *local* and *relative* file links into
        url_for(...) links. If images, css or javascript references point to
        websites, then leave them as they are

    4. Render the html file with your flask app

    5. Delete parts that you don't need

    6. Exchange parts like images or text with static or dynamic content of
        your own


---

----------------------------------------------
__ General Tips for using Templates + Flask __
----------------------------------------------

1. Work step by step and reload the page (using command/ctrl + shift + r to
    avoid using the cache; or use in incognito mode)

2. Consider saving a back up after you've put in some work. You might break
    things by deleting a single character accidentally. You really don't want
    to search for the mistake and you might have to start over.

3. I would not encourage you to build entire website like this. Using Flask
    like this should most of all just be done for creating  a nicer interface
    to an app where the key value driving factor is whats happening in the
    background. If you are building something that revolves more around the
    interface the rather use Flask + Bootstrap to keep things simpler


---

Template used in this example from:
http://www.mashup-template.com/preview.html?template=mountain

"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/step0")
def step0():
    return render_template("step0.html")


@app.route("/step1")
def step1():
    return render_template("step1.html")


@app.route("/step2")
def step2():
    return render_template("step2.html")


@app.route("/step3")
def step3():
    return render_template("step3.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
