# import turtle, random and Screen
from turtle import Screen
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

# declaire color_list

color_list = [(25, 108, 164), (194, 38, 81), (238, 161, 49), (234, 215, 85), (226, 237, 228), (223, 137, 176),
              (144, 108, 56), (102, 197, 219), (206, 166, 29), (20, 57, 132), (214, 73, 90), (239, 89, 50),
              (141, 208, 227), (118, 192, 140), (3, 186, 176), (106, 107, 199), (138, 29, 73), (4, 161, 86),
              (98, 51, 36), (22, 156, 210), (232, 165, 184), (175, 185, 221), (29, 90, 95), (233, 172, 161),
              (152, 213, 190), (242, 205, 8), (89, 48, 31)]


# make a draw circle function that gets a random color from the list and creates a size 20 circle
def random_circle():
    r_color = random.choice(color_list)
    tim.pencolor(r_color)
    tim.pendown()
    tim.pensize(20)
    tim.circle(10)
    tim.fillcolor(r_color)

tim.speed("fastest")
tim.penup()
tim.goto(0, -200)

for i in range(10):
    for i in range(10):
        random_circle()
        tim.penup()
        tim.forward(50)
    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.right(90)
    tim.right(90)





screen = t.Screen()
screen.exitonclick()
