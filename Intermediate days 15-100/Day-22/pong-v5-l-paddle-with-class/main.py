# imports
from turtle import Screen, Turtle
from paddle import Paddle
# Create the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
# create r and l paddle from the turtle class, pass in tuple for location
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
screen.exitonclick()


# TODO Create the ball and move it
# TODO detect collision with the wall and bounce
# TODO detect collision with paddle
# TODO detect when paddle misses
# TODO keep score


