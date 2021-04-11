from turtle import Turtle, Screen

tim = Turtle()
# create screen object
screen = Screen()

def move_forward():
    tim.forward(100)

# tell screen to start listening
screen.listen()
# add the event listener method
# screen.onkey()
# bind a function that will be triggered when a key is pressed on
# keyboard
# when the space key is pressed move forward 10
# don't put parens after function so that it dosen't run until space bar is pressed
screen.onkey(key="space", fun=move_forward)

screen.exitonclick()