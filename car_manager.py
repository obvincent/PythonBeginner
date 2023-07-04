import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 6) == 1: #This will create a car every 6 loops
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS)) 
            new_car.shapesize(stretch_wid = 1, stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(320, random.randint(-250,250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.forward(self.speed)
    
    def increase_speed(self):
        self.speed += MOVE_INCREMENT
