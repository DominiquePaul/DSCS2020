from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world!"


# Responses can also be made up of HTML.
#
# Note: HTML is a markup language used for creating websites. Its very simple
# to use and principally just consists of specific 'tags', like the header tag
# below for headlines
@app.route("/html-example")
def html_example():
    return "<h1>Hello world!</h1>"


@app.route("/welcome")
def welcome():
    return "Welcome to my webapp"


# If you look closely at urls for some services you will that some elements of
# the url are variable and contain your name or user ID e.g.
# instagram.com/natgeo/
#
# flask also supports this type of formatting and passes the dynamic content on
# to the function. Dynamic contents can be specificied using angular brackets
# and have to be specified as function argument
@app.route("/welcome/<name>")
def welcome_user(name):
    response = f"Welcome to my webapp {name}"
    return response


# Errors can be displayed very differently depending on whether you are using
# debug mode or not. In either case the app crashes, but if you have debug mode
# turned then it will display the error message.
# This is useful, but shouldn't be used in non-development versions, because
# it can expose sensitive data and expose security issues in your app
@app.route("/error")
def error_route():
    return 1/0


@app.route("/goodbye")
def goodbye():
    return("goodbye user!")


# debug mode
# the debug mode does two things when activated. (1) it reloads the app as soon
# as the underlying code changes and (2) it displays error message in the
# browser when something goes wrong
#
# port
# The port is a specific communication endpoint of a device in a network. By
# default, flask runs the app on port 5000, but you can change this. All
# websites use this concept, but often you don't see this because the websites
# you use run on the default port of the webadress (port 80).
#
# host
# The host argument tells the app which network it should listen to for
# requests. Per default it is 'localhost' which means that only requests
# coming from the same computer or server will be listened to. If we change
# the host to 0.0.0.0 then this anybody who reaches the app via a network can
# access it. This is especially important when you run your app on a server
# where you want to make it available to people connecting to this app via the
# public inte
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
