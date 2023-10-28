import random
import turtle

import colorgram
from turtle import Turtle, Screen


turtle.colormode(255)


my_screen = Screen()
my_screen.setup(width=600, height=600)
merki = Turtle()
merki.speed(0)
merki.hideturtle()
merki.penup()


colors = colorgram.extract("imagen.jpg", 30)
rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

rgb_colors = rgb_colors[3:]


def paint_line():
    for _ in range(10):
        merki.pendown()
        merki.dot(20, random.choice(rgb_colors))
        merki.penup()
        merki.forward(50)


start_x = -235
start_y = -225

merki.goto(start_x, start_y)
for i in range(10):
    paint_line()
    start_y += 50
    merki.goto(start_x, start_y)


my_screen.exitonclick()
