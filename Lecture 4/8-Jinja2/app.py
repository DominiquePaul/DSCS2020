# Jinja is a web template engine for the Python programming language that
# allows you to add some basic logic to your website content
# https://jinja.palletsprojects.com/en/2.11.x/

from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("1-basic.html")


# Inserting variables in html files
#
# Lets imagine we're setting up a digital ordering website for the ad hoc. We
# might also want to use the same website for the meeting point, so we want to
# keep the structure the same and be able to dynamically ingest variable names
@app.route("/variables1/<myname>")
def variables1(myname):
    return render_template("2-variables1.html",
                           company="Ad Hoc",
                           user=myname)


# Working with lists
#
# In the first step we want to display the name of the bartender and a
# short menu
@app.route("/variables2")
def variables2():
    bar_employees = ["Martha", "Lisa", "Alan"]
    bar_products = {"Beer": 4.50,
                    "White Wine": 8.5,
                    "Moscow Mule": 12.0}

    return render_template("3-variables2.html",
                           company="Ad Hoc",
                           employees=bar_employees,
                           products=list(bar_products.keys()),
                           prices=list(bar_products.values()))


# Basic logic
#
# The website has been getting some traffic, but some people have tried
# pre-ordering drinks when the bar wasnt open yet. Maybe we should hide the
# menu when the bar isn't open. We are going to need some basic logic in our
# html template for that
@app.route("/basic-logic")
def basic_logic():
    bar_employees = ["Martha", "Lisa", "Alan"]
    bar_products = {"Beer": 4.50,
                    "White Wine": 8.5,
                    "Moscow Mule": 12.0}

    hour_of_day = datetime.datetime.now().hour

    return render_template("4-basic_logic.html",
                           company="Ad Hoc",
                           employees=bar_employees,
                           products=list(bar_products.keys()),
                           prices=list(bar_products.values()),
                           hour_of_day=hour_of_day)


# for loops in html
#
# The head of Bereich G really likes the progress on the website. She gave us a
# longer list of products to add and she said there's a longer list to come.
# Oh no! That means we'd have to retype the menu every time! Luckily there's
# an easier way of displaying the list
@app.route("/for-loop")
def for_loop():
    bar_employees = ["Martha", "Lisa", "Alan"]
    bar_products = {"Schützengarten": 4.50,
                    "Klosterbräu": 4.50,
                    "White Wine": 8.5,
                    "Red Wine": 8.5,
                    "Moscow Mule": 12.0,
                    "Gin Tonic": 13.0
                    }

    hour_of_day = datetime.datetime.now().hour

    return render_template("5-for_loops.html",
                           company="Ad Hoc",
                           employees=bar_employees,
                           products=bar_products,
                           hour_of_day=hour_of_day)


if __name__ == "__main__":
    app.run(debug=True)
