from turtle import Turtle
SCORE_FONT = ("cascadia code", 12, "normal")


class LevelBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.show_score()

    def increase(self):
        self.level += 1
        self.reset()
        self.show_score()

    def show_score(self):
        self.color("black")
        self.penup()
        self.goto(-275, 275)
        self.write(f"Level:{self.level}", False, align="left", font=SCORE_FONT)
        self.hideturtle()

    def game_over(self):
        self.reset()
        self.color("black")
        self.hideturtle()
        self.write(f"Oops! GAME OVER {chr(10)}Level: {self.level}{chr(10)}Press 'r' to Replay", False, align="center", font=SCORE_FONT)

    def reset_score(self):
        self.level *= 0
        self.reset()
        self.show_score()
