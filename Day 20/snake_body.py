from turtle import Turtle
MOVE_FORWARD = 20

class SnakeBody:

    @classmethod
    def __init__(self):
        self.snake = []
        self.LOCATION = 20
        self.createsnake()
        self.head = self.snake[0]


    @classmethod
    def createsnake(self):
        for position in range(3):
            snakesq = Turtle(shape='square')
            snakesq.color("white")
            snakesq.penup()
            self.LOCATION = self.LOCATION - 20
            snakesq.goto(self.LOCATION, 0)
            self.snake.append(snakesq)
    @classmethod
    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment - 1].xcor()
            new_y = self.snake[segment - 1].ycor()
            self.snake[segment].goto(new_x, new_y)
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
