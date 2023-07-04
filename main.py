import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#SetUp Scoreboard, Screen, and Player
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    
    #Generate and move the cars
    cars.create_car()
    cars.move_cars()
    
    #Detect if we were hit by the first car and stop the game if it happens
    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    #Reset the Turtle when he makes it to the other side and update the scoreboard
    if player.ycor() >= 300:
        player.go_to_start()
        scoreboard.update()
        cars.increase_speed()

screen.exitonclick()