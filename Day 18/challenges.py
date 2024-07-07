from turtle import Turtle, Screen
import random

mzrh = Turtle()
screen = Screen()



# For Challenge 1 = Make a square from turtle
# for _ in range(4):
#     mzrh.pensize(10)
#     mzrh.forward(100)
#     mzrh.left(90)


# For Challenge 2 = Make it a Dashed Line
# for _ in range(15):
#     mzrh.forward(10)
#     mzrh.penup()
#     mzrh.forward(10)
#     mzrh.pendown()


# For Challenge 3 = Make it a Triangle to Decagon on same line and different Colours
# colours = ["red", "green", "blue", "orange", "pink", "gold", "yellow", "brown", "black", "purple"]
# for move in range(3, 11):
#
#     angles = 360 / move
#     for shapes in range(move):
#         mzrh.right(angles)
#         mzrh.forward(100)
#     clr = random.choice(colours)
#     mzrh.pencolor(clr)
#     # mzrh.forward(100)


# # For Challenge 4 = Make a Random Walk of the Turtle and Change thickness too
# direction = [0, 90, 180, 270]
# mzrh.speed('fast')
# for _ in range(200):
#     mzrh.pensize(10)
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     screen.colormode(255)
#     mzrh.pencolor(r, g, b)
#     mzrh.forward(30)
#     angle = random.choice(direction)
#     mzrh.setheading(angle)


# # For Challenge 5 = Draw a Spirograph
# for _ in range(90):
#     mzrh.speed('fastest')
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     screen.colormode(255)
#     mzrh.pencolor(r, g, b)
#     mzrh.circle(100)
#     mzrh.left(4)








screen.exitonclick()
