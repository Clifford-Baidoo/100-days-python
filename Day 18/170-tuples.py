from turtle import Turtle,Screen
import turtle as t
import random

tim = Turtle()
screen = Screen()
t.colormode(255)

tim.shape("turtle")
tim.pensize(15)
tim.speed("fastest")

directions = [0,90,180,270]


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

for i in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen.exitonclick()
    