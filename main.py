import random
import turtle as T
from turtle import Turtle, Screen
from color_extraction import rgb_colors

jim = T.Turtle()
T.colormode(255)
jim.penup()
jim.speed("fastest")
jim.hideturtle()
jim.left(225)
jim.forward(300)
jim.setheading(0)


for a in range(1, 101):
    jim.dot(20, random.choice(rgb_colors))
    jim.forward(50)

    if a % 10 == 0:
        jim.setheading(90)
        jim.forward(50)
        jim.setheading(180)
        jim.forward(500)
        jim.setheading(0)

screen = T.Screen()
screen.exitonclick()
