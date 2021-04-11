from turtle import Turtle, Screen
from random import randint

screen = Screen()

# set screen size using setup method
screen.setup(width=500,height=400)
# set the output of the screen.textinput() to user_bet
user_bet =screen.textinput(title="Make your bet", prompt="Who do you think will win the race? :")
colors =["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(0, 6):
    y_val = randint(-90, 90)
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-230, y_val )




tim = Turtle("turtle")
tim.penup()

# set the turtles to start position
#goto(x,y) needs coordinates
# tim.goto(-230, 100)
# or
tim.goto(x=-230, y=100)

screen.exitonclick()