from flask import Flask
app = Flask(__name__)

print(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# a common way to run a Flask app
#  tap into app and call run method
# app.run does the same thing as going to the terminal and
# executing flask run
# But with flask run, we have to provide the FLASK_APP environment variable
# and we have to stop the code using control + c instead of using our normal run and stop.
#  With app.run, can use standard controls, run to run this hello.py,
#  -it will start serving up Flask app just as before, when we did flask run.
#  Instead of using control + c to quit, can use the stop to stop our Flask application.
if __name__ == "__main__":
    app.run()