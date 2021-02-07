# set up inports 
from turtle import Turtle, Screen
from random import randint

 
screen = Screen()

# set screen size using setup method
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# list of tuples representing the starting position
starting_positions =[(0, 0) ,(-20, 0), (-40, 0)]

#new turtle 3 20x20 3 squares lined up on the horizon
for position in starting_positions:
    snake =Turtle("square")
    snake.color("white")
    snake.goto(position)
# condents this into a for  loop 
# new_turtle = Turtle("square")
# new_turtle.penup()
# new_turtle.color("white")
# new_turtle.goto(0, 0)
# new_turtle = Turtle("square")
# new_turtle.penup()
# new_turtle.color("white")
# new_turtle.goto(-20,0 )
# new_turtle = Turtle("square")
# new_turtle.penup()
# new_turtle.goto(-40, 0)
# new_turtle.color("white")

# keep screen open untill you click on it 
screen.exitonclick()