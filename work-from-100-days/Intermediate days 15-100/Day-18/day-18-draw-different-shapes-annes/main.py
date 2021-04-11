from turtle import Screen
import turtle as t
import random

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

colors = ["red","green","blue","orange","purple","pink","dark slate gray","magenta","light sky blue","medium spring green"]

sides=3
circle = 360


tim.pendown()

while sides <10:
    color = random.choice(colors)
    for _ in range(sides):
        tim.color(color)
        tim.forward(100)
        tim.right(circle/sides)
    sides +=1



















screen = Screen()
screen.exitonclick()