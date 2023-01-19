import random
from turtle import Turtle, Screen

jimmy = Turtle()
jimmy.shape("turtle")
jimmy.color("blueviolet")
colors = ["brown", "khaki", "wheat", "yellow", "orange", "tan", "red2", "dark green", "indigo", "firebrick"]

d = 360
for i in range(3,11):
    angle = d/i
    jimmy.color(random.choice(colors))
    while i != 0:
        jimmy.forward(100)
        jimmy.right(angle)
        i -= 1



screen = Screen()

screen.exitonclick()
