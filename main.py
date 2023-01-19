import random
from turtle import Turtle, Screen

jimmy = Turtle()
jimmy.shape("turtle")
jimmy.color("blueviolet")
colors = ["brown", "khaki", "wheat", "yellow", "orange", "tan", "red2", "dark green", "indigo", "firebrick"]
jimmy.pensize(10)
jimmy.speed(20)
for i in range(3, 110):
    jimmy.color(random.choice(colors))
    jimmy.forward(20)
    dir = random.choice([1, 2])
    if dir == 1:
        jimmy.right(90)
    else:
        jimmy.left(90)






screen = Screen()

screen.exitonclick()
