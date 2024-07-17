from turtle import Turtle
DISPLAY_FONT = ("Arial", 8, "normal")
CONGRATS_FONT = ("Chicle", 15, "normal")

class NameDisplay(Turtle):
    def __init__(self):
        super().__init__()

    def show_name(self, x_cor, y_cor, name):
        self.color("black")
        self.penup()
        self.goto(x_cor, y_cor)
        self.write(f"{name}", False, align="center", font=DISPLAY_FONT)
        self.hideturtle()

    def congratulations(self):
        self.color("black")
        self.penup()
        self.goto(0,0)
        self.write(f"Congratulations!, You've Guessed all Names Correctly.", False, align="center", font=CONGRATS_FONT)
        self.hideturtle()

    def onexit(self, score):
        self.color("black")
        self.penup()
        self.goto(0,0)
        self.write(f"You've Guessed {score}/29 States Correctly.", False, align="center", font=CONGRATS_FONT)
        self.hideturtle()