from turtle import Turtle,Screen
import random

tim = Turtle()
tim.shape("turtle")


screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0,256)
    g = random.randint(0,256)
    b = random.randint(0,256)
    return (r,g,b)

shape = True
sides = 3


while shape:
    angle = 360 / sides
    tim.color(random_color())
    for i in range(sides):
        tim.forward(100)
        tim.right(angle)
    sides += 1
    if sides == 11:
        shape = False




screen.exitonclick()