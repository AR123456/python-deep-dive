from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        #attributes for move()
        self.x_move = 10
        self.y_move = 10
        # attribute to control ball speed
        self.move_speed = 0.2


    def move(self):
         new_x = self.xcor() + self.x_move
         new_y = self.ycor() + self.y_move
         self.goto(new_x, new_y)
    def bounce_y(self):
        self.y_move *= -1
    #    speed up ball
        self.move_speed *= 0.9
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        # reset the move_speed after a score
        self.move_speed = 0.2
        self.bounce_x()




