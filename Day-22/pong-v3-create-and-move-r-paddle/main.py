#imports
from turtle import Screen,Turtle
#
import time
# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
# turn the screen off to not see the paddle move from center
# to its position on the right at start to game.
# when useing screen.tracer will need to turn it back on in the
# while loop below while game_is_on
screen.tracer(0)
# Create and move  R paddle
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)
def go_up():
    #the current y position of the paddle + 20
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)
def go_down():
    new_y = paddle.ycor() -20
    paddle.goto(paddle.xcor(), new_y)
screen.listen()
#when passing in a function as a paramater omit the parens
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

# TODO Create L paddle
# TODO Create the ball and move it
# TODO detect collision with the wall and bounce
# TODO detect collision with paddle
# TODO detect when paddle misses
# TODO keep score

screen.listen()

screen.exitonclick()
