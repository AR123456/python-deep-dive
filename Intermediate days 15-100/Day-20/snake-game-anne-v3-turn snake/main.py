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
    # for i in segments:
    #     i.forward(20)
    # change loop so that it goes from last to first, in reverse order
    # use the range type of for loop and pass in start,stop and step
    # start is number we are going to start the range from
    # stop is where the range is going to end
    # step is how we are going to get from start to stop
    # note range cannot take keyword args so this is just for example
    #for i in range(start=2 ,stop= 0,step= -1):
    # now changing the hard coded numbers to vars so that as the snake grows
    # that is the segments list gets longer game will still work
    # for i in range(2, 0, -1):
    for i in range(len(segments)-1, 0, -1):
        new_x=segments[i-1].xcor()
        new_y=segments[i -1].ycor()
        segments[i].goto(new_x, new_y)
    # outside of the for loop get hold of the first value in the segments list move it 20
    segments[0].forward(20)
    # turn the first segment left
    segments[0].left(90)

 
screen.exitonclick()