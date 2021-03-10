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
# use a converter to specify the type of the argument like <converter:variable_name>.
# can be string, int float, path, uuid - default is string
# you can also have more than one variable
@app.route("/<name>/<int:number>")
def greet(name,number):
    return f"Hello {name}, you are {number} years old!"


if __name__ == "__main__":
    # putting Flask into debug mode
    app.run(debug=True)
