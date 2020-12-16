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
# control the snake with the arrow keys
screen.listen()
# key bindings strings for arrow keys,bind to function in snake object
# that has the same name
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    # once all segments have moved calling update
    screen.update()
    # slow the snake down
    time.sleep(0.1)
    snake.move()


screen.exitonclick()