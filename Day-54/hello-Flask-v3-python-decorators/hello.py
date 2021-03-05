from flask import Flask
app = Flask(__name__)

print(__name__)
# Python Decorator -  /
# go to the home route
#  A decorator function is a function gives additional functionality to an existing function
@app.route('/')
def hello_world():
    return 'Hello, World!'

# run the Flask app
if __name__ == "__main__":
    app.run()