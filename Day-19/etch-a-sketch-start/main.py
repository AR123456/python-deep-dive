from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.setheading(0)
    tim.forward(50)
def move_backwards():
    tim.setheading(180)
    tim.forward(50)

def move_clockwise():
    tim.setheading(90)
    tim.forward(50)

def move_counter_clockwise():
    tim.setheading(270)
    tim.forward(50)

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c",fun=tim.clear)

screen.exitonclick()
