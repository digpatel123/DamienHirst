from turtle import Turtle, Screen

jimmy = Turtle()
jimmy.shape("turtle")
jimmy.color("blueviolet")
for i in range(4):
    jimmy.forward(200)
    jimmy.right(90)

screen = Screen()

screen.exitonclick()
