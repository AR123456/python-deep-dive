# imports
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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
#create scoreboard
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    #time.sleep being shorter will speed up the game
    # time.sleep(0.2)
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor()>280 or ball.ycor()< -280:
        ball.bounce_y()
    #Detect collision with r_paddle
    if ball.distance(r_paddle)< 50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor() < -320:
       ball.bounce_x()
    #Detect when R paddle misses
    if ball.xcor()> 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect when L paddle misses
    if ball.xcor()< -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()




