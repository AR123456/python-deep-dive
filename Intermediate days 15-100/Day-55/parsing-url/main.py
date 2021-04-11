from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

# route decorator or the route to look for when a user goes to a particular path
@app.route("/bye")
def bye():
    return "Bye!"

if __name__ == "__main__":
    app.run()
