# redirects are responses that do not include a webpage but send the user to a
# different web address.
# This is e.g. useful when you first check for a condition in a function, like
# whether the user is logged in or not, and based on that send the user
# to another webpage or show them the regular content

from flask import Flask, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world!"


@app.route("/sign-in")
def signin():
    return "Please sign in first"


@app.route("/user/<id>")
def show_content(id):
    id = int(id)
    if id in [1, 2, 3, 4]:
        return f"Hello user {id}!"
    else:
        return redirect("http://0.0.0.0:5000/sign-in")


@app.route("/redirect")
def simple_redirect():
    return redirect("http://www.google.com")


if __name__ == "__main__":
    app.run(debug=True)
