from turtle import Screen
import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colors = ["red","green","blue","orange","purple","pink","dark slate gray","magenta","light sky blue","medium spring green"]
moves = [ 0,90,180,270]
strides=0
color = random.choice(colors)
move = random.choice(moves)


while strides<30:
    tim.pendown()
    tim.width(10)

    for _ in range(strides):
        tim.color(random.choice(colors))
        tim.forward(40)
        tim.setheading(random.choice(moves))
        tim.speed(random.randrange(10))
    strides += 1






screen = Screen()
screen.exitonclick()