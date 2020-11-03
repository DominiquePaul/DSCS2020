from flask import Flask

supercoolapp = Flask(__name__)


@supercoolapp.route("/")
def index():
    return "Hello DSCS!"


if __name__ == "__main__":
    supercoolapp.run(host="0.0.0.0", port=80)
