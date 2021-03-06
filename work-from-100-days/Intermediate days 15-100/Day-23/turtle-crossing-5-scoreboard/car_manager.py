from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        #add attribute
        self.car_speed = STARTING_MOVE_DISTANCE
    def create_car(self):
        #slow the generation of new car creation by one 6ths
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            # random position on the y axis
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            # append to the car list
            self.all_cars.append(new_car)
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


