from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

# route decorator or the route to look for when a user goes to a particular path
@app.route("/bye")
def bye():
    return "Bye!"
#adding variable to route
#You can add variable sections to a URL by marking sections with <variable_name>.
# Your function then receives the <variable_name> as a keyword argument.
# Optionally, you can use a converter to specify the type of the argument
# like <converter:variable_name>.
#flask will treat what comes after username in the angle brackets as a variable
@app.route("/<name>")
def greet(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    # putting Flask into debug mode
    app.run(debug=True)
