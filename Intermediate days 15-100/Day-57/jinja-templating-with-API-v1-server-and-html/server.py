import random
import datetime
import requests
# boiler plate to spin up the server
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home_route():
    return "<h1>Guess and I will guess your age and gender</h1>"

@app.route("/guess")
def guess_rote():
    return render_template("index.html")
if __name__ =="__main__":
    app.run(debug=True)