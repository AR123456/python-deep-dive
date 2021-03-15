# boiler plate to spin up the server
from flask import Flask
app = Flask(__name__)
@app.route("/")
def home_route():
    return "<h1>Home route</h1>"

if __name__ == "__main__":
    app.run(debug=True)