from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    # get current heading and turn left towards by 10 
    # or tim.left(10)
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    #get current heading and turn right by 10
    # or tim.right(10)
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    # this clear is bound to the turtle
    tim.clear()
    # bring turlte back to starting point, pick pen up first
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")

screen.exitonclick()
