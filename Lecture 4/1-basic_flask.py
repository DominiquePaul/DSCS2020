from flask import Flask

# initialisation
app = Flask(__name__)


# first webaddress. '/' stands for home
@app.route("/")
def index():
    return "Hello world!"


@app.route("/html")
def html():
    return """<h1>Hello world!</h1>
                <p> welcome</p>
                """


# We only want the app to run when this script is executed explicitly
# (i.e. it isn't imported)
app.run()
