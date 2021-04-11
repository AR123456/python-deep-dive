import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#create player instance
player = Player()

# move player
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor() >280:
        player_level_up()







 
# #TODO detect collision with top wall and turtle 
#  #TODO increase level when the collision occurs
#   #TODO put turtle back at bottom edge of screen(starting position)

#    #TODO create cars
#TODO create a car that is 2 boxes in size
#TODO randomly give it a color
# #TODO at increments along the far left create cars space a cars width apart randomly
#TODO move car(s) accross screen at a speed that will increase with each level up
#TODO detect collison with turtle
#TODO show game over


screen.exitonclick()
