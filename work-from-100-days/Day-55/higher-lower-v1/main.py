from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    # adding HMGL and CSS to the return
    return "<h1 style='text-align: center'>Guess a number between 0 and 9</h1>" \
           "<p>This is a paragraph.</p>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width=200></img>"


# route decorator or the route to look for when a user goes to a particular path

@app.route("/bye")
def bye():
    return "Bye!"

@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"


if __name__ == "__main__":
    # putting Flask into debug mode
    app.run(debug=True)
