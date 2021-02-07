from turtle import Turtle
STARTING_POSITION = (0, -280)
#move distance goes up with each level up
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
#Turtle that crosses the road movement is only the up arrow key
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.left(90)
        self.penup()
        self.goto(STARTING_POSITION)


