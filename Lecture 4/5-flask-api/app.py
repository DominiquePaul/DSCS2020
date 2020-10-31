# Remember how we used APIs last time?
# We can actually now create our own API for others using flask

from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def index():
    return "App is running"


# One way of collecting input is by using variables that are passed in the url
# itself. This is a nice and simple way, but can also be cumbersome if you have
# a lot of variables
@app.route("/math/<int:num1>/<int:num2>")
def math(num1, num2):
    return str(num1 * num2)


# a second way is by requiring parameters to be sent with the request
@app.route("/math2")
def math2():
    # num1 = request.args["num1"]
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')

    if (num1 is None) or (num2 is None):
        return "Please submit valid parameters"

    return str(int(num1) * int(num2))


# If you ask for parameters, you will want to check that they were really sent
# with the request, as your app might crash otherwise
@app.route("/math3")
def math3():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')

    if (num1 is None) or (num2 is None):
        return {"response": "Please submit valid parameters"}

    mydict = {"response": str(int(num1) * int(num2)),
              "sum": str(int(num1) + int(num2))}

    return mydict


# Requests arent the most efficient method though, especially if there are a
# lot of requests, the data sent is more complicated and when some of the data
# is confidential
@app.route("/math4", methods=["POST"])
def math4():
    data = request.json
    numlist = data["nums"]

    result = 1

    for element in numlist:
        result *= element


    return {"Product": result}


if __name__ == "__main__":
    app.run(debug=True)
