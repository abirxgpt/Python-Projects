from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_paddle()
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1
    def create_paddle(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce(self):
        self.ymove *= -1

    def paddle_bounce(self):
        self.xmove *= -1
        self.move_speed -= 0.01

    def reset_pos(self):
        self.goto(0,0)
        self.paddle_bounce()

    def speed_reset(self):
        self.move_speed = 0.1