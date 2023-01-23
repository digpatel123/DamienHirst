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


directions = [0, 90, 180, 270]
jimmy.pensize(10)
jimmy.speed(20)
for i in range(200):
    jimmy.color(random_color())
    jimmy.setheading(random.choice(directions))
    jimmy.forward(20)






screen = Screen()

screen.exitonclick()
