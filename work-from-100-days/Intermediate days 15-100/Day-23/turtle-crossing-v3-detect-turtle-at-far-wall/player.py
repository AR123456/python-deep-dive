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
        #attributes for move()

        self.y_move = MOVE_DISTANCE
        self.level=1

    def move(self):

        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)

    def player_level_up(self):
        self.level +=1
        self.goto(STARTING_POSITION)





