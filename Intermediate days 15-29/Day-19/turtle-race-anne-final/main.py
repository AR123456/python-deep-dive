from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()

# set screen size using setup method
screen.setup(width=500,height=400)
# set the output of the screen.textinput() to user_bet
user_bet =screen.textinput(title="Make your bet", prompt="Who do you think will win the race? :")
colors =["red", "orange", "yellow", "green", "blue", "purple"]
# need to use specific vals or y so that they are spaced out correctly
y_val = [-70, -40, -10, 20, 50, 80]
all_turtles=[]

for i in range(0, 6):

    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    print(y_val[i])
    new_turtle.goto(-230, y_val[i])
    # each new_turtle has different state
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won ! The {winning_color} turtle is the winner")
            else:
                print(f"You lost. the {winning_color} turtle is the winner ")
        rand_distance=randint(0, 10)
        turtle.forward(rand_distance)
# stopping  x val of 250 - size of turtle 40 /2  or 230

screen.exitonclick()