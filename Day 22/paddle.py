from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.create_paddle(pos)

    def create_paddle(self, position):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.left(90)
        self.goto(position)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)



