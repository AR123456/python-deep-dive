from turtle import Turtle
# const is in all caps
STARTING_POSITIONS =[(0, 0) ,(-20, 0), (-40, 0)]
# creating a const for the step forward
MOVE_DISTANCE = 20
# creating snake class
class Snake:
    def __init__(self):
        # for movement create an empty list of segments
        #use self when within a class
        self.segments = []
        self.create_snake()

    def create_snake(self):
        # starting_positions is now a const
        for position in STARTING_POSITIONS :
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            #segments is now self.segments
            self.segments.append(new_segment)
    def move(self):
        # segments is now self.segments
            for i in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[i - 1].xcor()
                new_y = self.segments[i - 1].ycor()
                self.segments[i].goto(new_x, new_y)
            self.segments[0].forward(MOVE_DISTANCE)










