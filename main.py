from turtle import Turtle, Screen

jimmy = Turtle()
jimmy.shape("turtle")
jimmy.color("blueviolet")
for i in range(10):
    jimmy.pendown()
    jimmy.forward(10)
    jimmy.penup()
    jimmy.forward(10)

screen = Screen()

screen.exitonclick()
