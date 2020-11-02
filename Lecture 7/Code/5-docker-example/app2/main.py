import requests
import datetime
from flask import Flask, render_template, redirect, url_for

from image_functions import get_city_img_link, write_img_to_disk

WEATHER_API_KEY = "8499f70709039a2222fa80c2c6e32430"

app = Flask(__name__)

#  we add the secret key for the form in part 4
app.config["SECRET_KEY"] = "23zujnnmjhgfdrtzuikmj"


@app.route("/")
def index():
    return redirect(url_for("homescreen",
                    name="Dominique",
                    location="Zurich",
                    goal="Create a Flask website"))


def get_weather(location):

    endpoint = "http://api.openweathermap.org/data/2.5/weather"
    parameters = {"q": location,
                  "appid": WEATHER_API_KEY,
                  "units": "metric"}
    r = requests.get(endpoint, params=parameters)

    # we can use html status code to check whether the request was successfull
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    # (This not a requirement for the assignment)
    if r.status_code == 200:
        data = r.json()
        result = {
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"]
        }

        return result
    else:
        return("There was an error retrieving the temperature for " +
               f"'{location}', please check your input and try again")


def weather(location):

    if location.lower() == "cologne":
        return redirect(url_for("hometown"))

    weather = get_weather(location)

    # create the text that we want to display
    text = f"The weather in {location} is {weather['description']} with a " +\
        f"humidity of {weather['humidity']}%. The temperature is " +\
        f"{weather['temperature']} degrees celsius but it feels like " +\
        f"{weather['feels_like']} degrees celsius"

    # you can also use this text in a template if you like
    return text


# we add the goal attribute for Part 4
@app.route("/homescreen/<name>/<location>/<goal>")
def homescreen(name, location, goal):

    weather_text = weather(location)

    # this does not have to be local time of the location, we are assuming
    # the time of the computer
    time = datetime.datetime.now().strftime('%H:%M')

    # download image file
    img_url = get_city_img_link(location)
    filename = location + "_img"
    write_img_to_disk(img_url, "static", filename)

    return render_template("index.html",
                           user_name=name,
                           location=location,
                           weather=weather_text,
                           time=time,
                           img_name=filename,
                           goal=goal)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
