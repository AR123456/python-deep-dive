# set up imports
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# to slow down the snake
import time

screen = Screen()
# set screen size using setup method
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# turn screen tracker off -
screen.tracer(0)
# create a new snake object from the class
snake = Snake()
# create food object from food class
food = Food()
# create scoreboard from scorboard class
scoreboard = Scoreboard()
# control the snake with the arrow keys
screen.listen()
# passing in methods from snake.py
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

    if snake.head.distance(food) < 45:
#   if snake.head.distance(food) < 15:
        # food should go to new random location
        food.refresh()
        # call scoreboard function
        scoreboard.increase_score()
#Detect collision with wall
    if snake.head.xcor()> 280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on =False
        scoreboard.game_over()


screen.exitonclick()
