import random
import datetime
import requests
# boiler plate to spin up the server
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home_route():
    return "<h1>Enter guess and your name and I will guess your age and gender</h1>"
# need to pars this url so putting name in angle brackets
#Flask documentaton
@app.route("/guess/<name>")
#pass name into guess
def guess(name):
    # gender api end point
    gender_url=f"https://api.genderize.io?name={name}"

    #using requests
    gender_response = requests.get(gender_url)
    # response in json
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    # for age
    age_url = f"https://api.agify.io/?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age=age_data["age"]

    return render_template("index.html", name=name, gender = gender, age=age)



if __name__ =="__main__":
    app.run(debug=True)