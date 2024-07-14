from turtle import Turtle
STEP = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_turtle()

    def create_turtle(self):
        self.shape("turtle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(x=0, y=-280)
        self.left(90)
        self.color("black")

    def ahead(self):
        self.forward(STEP)

    def behind(self):
        self.backward(STEP)

    def next_level(self):
        self.reset()
        self.create_turtle()

