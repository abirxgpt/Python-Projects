from turtle import Turtle
SCORE_FONT = ("cascadia code", 40, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_right = 0
        self.score_left = 0
        self.showscore()

    def increase_r(self):
        self.score_right += 1
        self.reset()
        self.showscore()

    def increase_l(self):
        self.score_left += 1
        self.reset()
        self.showscore()

    def showscore(self):
        self.color("white")
        self.penup()
        self.goto(0, 230)
        self.write(f"{self.score_left}         {self.score_right}", False, align="center",font=SCORE_FONT)
        self.hideturtle()