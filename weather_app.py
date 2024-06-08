from flask import Flask, render_template, request, redirect
import requests 

app = Flask(__name__)
API_KEY = "4ef09af5026b136636cbe2fb338e3503"


@app.route("/", methods = ["GET","POST"])
def home():
    if request.method == "POST":
        city = request.form.get("city")
        # Check if the user filled the form
        if city:
            # Pull weather data
            try:
                response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&appid={API_KEY}")
                celsius = response.json()["main"]["temp"]
                return render_template("city.html", city=city, celsius=celsius)
            except:
                return render_template("unknown_city.html")
    return render_template("index.html")


