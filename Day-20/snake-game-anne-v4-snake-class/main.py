# set up inports 
from turtle import Turtle, Screen
from snake import Snake
# to slow down the snake
import time
screen = Screen()
# set screen size using setup method
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# turn screen tracker off -
screen.tracer(0)
#create a new snake object from the class
snake = Snake()


game_is_on = True
while game_is_on:
    # once all segments have moved calling update
    screen.update()
    # slow the snake down
    time.sleep(0.1)
    snake.move()


screen.exitonclick()