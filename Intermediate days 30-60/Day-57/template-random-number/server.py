import random
# boiler plate to spin up the server
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home_route():
    #puting the random number generator in the home route
    random_number = random.randint(1,10)
    #send random_number as keword arg , the arg gets passed to HTML in route
    return render_template("index.html", num=random_number)
if __name__ =="__main__":
    app.run(debug=True)