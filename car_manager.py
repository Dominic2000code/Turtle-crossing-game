from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.create_car()
        self.current_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.setheading(180)
        car.goto(300, random.randint(-250, 250))  # Adjust starting position
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.current_speed)

    def level_up(self):
        self.current_speed += MOVE_INCREMENT
