from turtle import Turtle
MOVE_FORWARD = 20
LOCATION = [(0, 0), (-20, 0), (-40, 0)]
class SnakeBody:
    @classmethod
    def __init__(self):
        self.segment = []
        self.createsnake()
        self.head = self.segment[0]

    @classmethod
    def createsnake(self):
        for position in LOCATION:
            self.add_part(position)

    @classmethod
    def add_part(self, position):
        snakesq = Turtle(shape='square')
        snakesq.color("white")
        snakesq.penup()
        snakesq.goto(position)
        self.segment.append(snakesq)

    @classmethod
    def adding(self):
        print(self.segment[-1].position())
        self.add_part(self.segment[-1].position())

    @classmethod
    def move(self):
        for segment in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[segment - 1].xcor()
            new_y = self.segment[segment - 1].ycor()
            self.segment[segment].goto(new_x, new_y)
        self.head.forward(MOVE_FORWARD)

    @classmethod
    def forward(self):
        if self.head.heading() == 0.0:
            self.head.left(90)
        elif self.head.heading() == 180.0:
            self.head.right(90)

    @classmethod
    def backward(self):
        if self.head.heading() == 0.0:
            self.head.right(90)
        elif self.head.heading() == 180.0:
            self.head.left(90)

    @classmethod
    def lefty(self):
        if self.head.heading() == 90.0:
            self.head.left(90)
        elif self.head.heading() == 270.0:
            self.head.right(90)

    @classmethod
    def righty(self):
        if self.head.heading() == 90.0:
            self.head.right(90)
        elif self.head.heading() == 270.0:
            self.head.left(90)

    @classmethod
    def reset_snake(self):
        for body in self.segment:
            body.goto(999,999)
        self.segment.clear()
        self.createsnake()
        self.head = self.segment[0]
