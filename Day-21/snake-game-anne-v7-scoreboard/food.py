from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        # need call to superclass
        super().__init__()
        # now can use stuff from the turtle class like shape
        self.shape("circle")
        self.penup()
        # 10x10 size
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.shapesize(stretch_len= 5, stretch_wid=5)
        self.color("blue")
        # so animation is not slowed down when dot moves
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # jump to random location on 600x600 screen
        # to allow space -280 to 280
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
