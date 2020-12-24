from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        #attributes for move()
        self.x_move =10
        self.y_move =10


    def move(self):
        # replaceing hard coded with attributes
        # new_x = self.xcor() + 18
        # new_y = self.ycor() + 18
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    def bounce(self):
        # move needs to be to opposite
        # multiply by -1 will change it to its opposite
        self.y_move *= -1


