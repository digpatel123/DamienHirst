import random
import turtle
from turtle import Turtle, Screen

jimmy = Turtle()
jimmy.shape("turtle")
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

jimmy.speed("fastest")
angle = 0
for i in range(72):
    jimmy.setheading(angle)
    jimmy.color(random_color())
    jimmy.circle(100)
    angle += 5

screen = turtle.Screen()
screen.exitonclick()
