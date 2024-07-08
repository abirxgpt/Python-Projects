from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width= 500, height= 500)
on_race = True


user_bet = screen.textinput(title="Place your Bet", prompt="Which Turtle will win the race?, Choose your bet: ")
colours = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
y_direction = [-155, -95, -35, 25, 85, 145, 205]
all_turtles = []
for turtle_index in range(7):
    turt = Turtle(shape="turtle")
    turt.color(colours[turtle_index])
    turt.penup()
    turt.goto(x=-230, y=y_direction[turtle_index])
    all_turtles.append(turt)


while on_race:
    for turtle in all_turtles:
        speedturt = random.randint(0, 10)
        turtle.forward(speedturt)
        if turtle.xcor() > 230:
            on_race = False
            win = turtle.pencolor()
            if user_bet.lower() == win:
                print(f"You've Won!, The {win} Turtle has won the Race")
            else:
                print(f"You've Lost!, The {win} Turtle has won the Race")

screen.exitonclick()
