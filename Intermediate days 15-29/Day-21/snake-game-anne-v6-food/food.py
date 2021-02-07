from turtle import Turtle
import random
# want food class to inherit from the Turtle class so
# put the parens after Food pass in Turtle class
class Food(Turtle):
    def __init__(self):
        # need call to superclass
        super().__init__()
        # now can use stuff from the turtle class like shape
        self.shape("circle")
        self.penup()

        # 10x10 size
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        # self.shapesize(stretch_len= 5, stretch_wid=5)
        self.color("blue")
        # so animation is not slowed down when dot moves
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # jump to random location on 600x600 screen
        # x -300 to 300 to allow space -280 to 280
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        # y 300 to -300 to allow space 280 to -280
        self.goto(random_x, random_y)
