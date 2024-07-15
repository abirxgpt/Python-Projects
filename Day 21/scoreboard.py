from turtle import Turtle
SCORE_FONT = ("cascadia code", 12, "normal")
GAME_OVER_FONT = ("times new roman", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as hs:
            self.highscore = int(hs.read())
        self.showscore()

    def increase(self):
        self.score += 1
        self.reset()
        self.showscore()

    def showscore(self):
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score:{self.score} | High Score:{self.highscore}", False, align="center", font=SCORE_FONT)
        self.hideturtle()

    def game_over(self):
        self.reset()
        self.color("white")
        self.hideturtle()
        self.write(f"Oops! GAME OVER {chr(10)}Score: {self.score}{chr(10)}Press 'R' to Play Again", False, align="center", font=GAME_OVER_FONT)

    def reset_game(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("high_score.txt", mode="w") as hs:
                hs.write(str(self.highscore))
        self.score = 0
        self.reset()
        self.showscore()

