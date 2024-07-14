from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.multiple_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.penup()
            car.left(180)
            car.shapesize(stretch_wid=1, stretch_len=2)
            y_pos = random.randint(-250, 250)
            car.goto(300, y_pos)
            self.multiple_cars.append(car)

    def move_car(self):
        for cars in self.multiple_cars:
            cars.forward(self.car_speed)

    def speed_increase(self):
        self.car_speed += MOVE_INCREMENT

    def reset_game(self):
        for cars in self.multiple_cars:
            cars.hideturtle()
        self.multiple_cars.clear()
        self.car_speed = STARTING_MOVE_DISTANCE
