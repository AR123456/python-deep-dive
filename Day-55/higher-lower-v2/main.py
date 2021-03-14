from flask import Flask
import random

random_number = random.randint(0, 9)
app = Flask(__name__)


@app.route("/")
def home_route():
    # adding HMGL and CSS to the return
    return "<h1 style='text-align: center'>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width=200></img>"


# Create a route that can detect the number entered by the user
# e.g "URL/3" or "URL/9" and checks that number against the generated random number.
# If the number is too low, tell the user it's too low,
# same with too high or if they found the correct number.
# try to make the <h1> text a different colour for each page.  e.g.
# If the random number was 5:

@app.route("/<int:guess>")
def guess(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>/" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    # putting Flask into debug mode
    app.run(debug=True)
