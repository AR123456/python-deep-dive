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
# create car manager
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up,"Up ")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    #with every screen update create a new car (0.1) secs
    car_manager.create_car()
    car_manager.move_cars()


screen.exitonclick()