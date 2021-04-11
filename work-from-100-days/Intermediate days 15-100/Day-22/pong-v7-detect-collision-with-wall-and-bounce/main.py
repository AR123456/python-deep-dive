# imports
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
#  to slow ball down import time to pause
import time
# Create the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
# create r and l paddle from the turtle class, pass in tuple for location
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# create ball
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    ball.move()
    # if the ball reaches y value of 300or -300 change
    if ball.ycor()>280 or ball.ycor()< -280:
        ball.bounce()


screen.exitonclick()


# TODO detect collision with the wall and bounce
# TODO detect collision with paddle
# TODO detect when paddle misses
# TODO keep score


