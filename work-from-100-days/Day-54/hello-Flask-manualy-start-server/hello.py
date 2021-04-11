from flask import Flask

# one required import __name__
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'