from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.createfood()
        self.randomize()

    def createfood(self):
        self.shape("circle")
        self.color("chartreuse")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.speed('fastest')

    def randomize(self):
        xcor = random.randint(-280, 280)
        ycor = random.randint(-280, 280)
        self.goto(x=xcor, y=ycor)
