from turtle import Turtle
# const is in all caps
STARTING_POSITIONS =[(0, 0) ,(-20, 0), (-40, 0)]
# creating a const for the step forward
MOVE_DISTANCE = 20
# making the cardinal dir consts
UP = 90
DOWN = 279
LEFT = 180
RIGHT = 0
# creating snake class
class Snake:
    def __init__(self):
        # for movement create an empty list of segments
        #use self when within a class
        self.segments = []
        self.create_snake()
        # creating an attribute for the head of the snake
        self.head =self.segments[0]

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
            self.head.forward(MOVE_DISTANCE)

    # move the head of the snake[0]
    def up(self):
      # if the current heading is pointed down dont allow
      # move up since that move is not allowed in the snake game
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)








