# from colorgram import colorgram
#
# rgb_colours = []
# colors = colorgram.extract('image_hirst.jpg', 30)
# for colour in colors:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     rgb = (r, g, b)
#     rgb_colours.append(rgb)
import random
from turtle import Turtle, Screen

hirst = Turtle()
scr = Screen()
scr.colormode(255)

rgb_colours = [(234, 166, 59), (45, 112, 157), (113, 150, 203), (212, 123, 164), (16, 128, 96), (172, 44, 88), (1, 177, 143), (153, 18, 54), (224, 201, 117), (225, 76, 115), (163, 166, 35), (28, 35, 84), (227, 86, 43), (42, 166, 208), (120, 172, 116), (119, 102, 158), (215, 64, 33), (237, 244, 241), (39, 52, 100), (76, 21, 45), (229, 169, 188), (14, 99, 71), (31, 61, 56), (8, 92, 107), (222, 177, 169), (181, 188, 208), (171, 203, 193)]
y = 0
hirst.penup()
hirst.hideturtle()
hirst.speed("fast")
for _ in range(10):
    for paint in range(10):
        colour = random.choice(rgb_colours)
        hirst.dot(20, colour)
        hirst.forward(50)
    y += 50
    hirst.setx(0)
    hirst.sety(y)

scr.exitonclick()

