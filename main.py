import random
import turtle
from turtle import Turtle, Screen

jimmy = Turtle()
jimmy.shape("turtle")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


jimmy.speed("fastest")
angle = 0


def spirograph(angle_gap):
    for i in range(int(360 / angle_gap)):
        jimmy.color(random_color())
        jimmy.circle(100)
        jimmy.setheading(jimmy.heading() + angle_gap)


spirograph(5)

screen = turtle.Screen()
screen.exitonclick()
