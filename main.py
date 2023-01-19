import random
from turtle import Turtle, Screen

jimmy = Turtle()
jimmy.shape("turtle")
jimmy.color("blueviolet")
colors = ["brown", "khaki", "wheat", "yellow", "orange", "tan", "red2", "dark green", "indigo", "firebrick"]
directions = [0, 90, 180, 270]
jimmy.pensize(10)
jimmy.speed(20)
for i in range(200):
    jimmy.color(random.choice(colors))
    jimmy.setheading(random.choice(directions))
    jimmy.forward(20)






screen = Screen()

screen.exitonclick()
