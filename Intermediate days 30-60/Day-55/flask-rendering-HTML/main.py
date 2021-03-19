from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    # adding HMGL and CSS to the return
    # return "Hello World"
    return "<h1 style='text-align: center'>Hello World!</h1>" \
           "<p>This is a paragraph.</p>" \
           "<img src='https://media3.giphy.com/media/aCqb9YW7QclN3rtto5/giphy.webp?cid=ecf05e47zpz4ehr3dpy9db8drnef05b3ked0wuntew9z8ru5&rid=giphy.webp' width=200></img>"


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
