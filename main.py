import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.up, "Up")

generate_car = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create a car every 6th time the loop runs
    if generate_car == 6:
        car_manager.create_car()
        generate_car = 0
    generate_car += 1

    car_manager.move_cars()

    # Detect if player reached end
    if player.ycor() >= FINISH_LINE_Y:
        player.reset_player_position()
        scoreboard.increment_level()
        car_manager.level_up()

    # Detect collision with car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
