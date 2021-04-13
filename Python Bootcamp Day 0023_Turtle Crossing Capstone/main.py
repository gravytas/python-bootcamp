import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

user = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(user.move, "Up")


game_on = True
while game_on:
    time.sleep(.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #detect collision with car
    for car in car_manager.all_cars:
        if car.distance(user) <= 20:
            game_on = False
            scoreboard.gameover()

    #detect successful crossing
    if user.crossed() == True:
        user.to_start()
        car_manager.level_up()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()





screen.exitonclick()