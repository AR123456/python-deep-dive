# set up inports 
from turtle import Turtle, Screen
from random import randint
# to slow down the snake
import time

 
screen = Screen()

# set screen size using setup method
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# turn screen tracker off - things are happening in code
# but it is not showing on screen.  screen.update will refresh the screen
# and show what has been happening.
screen.tracer(0)
starting_positions =[(0, 0) ,(-20, 0), (-40, 0)]
# for movement create an empty list of segments
segments = []

#new turtle 3 20x20 3 squares lined up on the horizon
for position in starting_positions:
    new_segment =Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    # once all segments have moved calling update
    screen.update()
    # slow the snake down
    time.sleep(0.1)
    for i in segments:
        # turn tracer off and update() screen so snake looks like a snake and not a catipiller
        i.forward(20)

screen.exitonclick()