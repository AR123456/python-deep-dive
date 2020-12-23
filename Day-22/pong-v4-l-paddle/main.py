#imports
from turtle import Screen, Turtle
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
paddle_r = Turtle()
paddle_r.shape("square")
paddle_r.color("white")
paddle_r.shapesize(stretch_wid=5, stretch_len=1)
paddle_r.penup()
paddle_r.goto(350, 0)

# Create and move  L paddle
paddle_l = Turtle()
paddle_l.shape("square")
paddle_l.color("white")
paddle_l.shapesize(stretch_wid=5, stretch_len=1)
paddle_l.penup()
paddle_l.goto(10, 0)

def go_up_r():
    #the current y position of the paddle + 20
    new_y_r = paddle_r.ycor() + 20
    paddle_r.goto(paddle_r.xcor(), new_y_r)
def go_down_r():
    new_y_r = paddle_r.ycor() - 20
    paddle_r.goto(paddle_r.xcor(), new_y_r)
def go_up_l():
    #the current y position of the paddle + 20
    new_y_l = paddle_l.ycor() + 20
    paddle_l.goto(paddle_l.xcor(), new_y_l)
def go_down_l():
    new_y_l = paddle_l.ycor() - 20
    paddle_l.goto(paddle_l.xcor(), new_y_l)

screen.listen()
#when passing in a function as a paramater omit the parens
screen.onkey(go_up_r, "Up")
screen.onkey(go_down_r, "Down")
screen.onkey(go_up_l, "Up")
screen.onkey(go_down_l, "Down")

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
