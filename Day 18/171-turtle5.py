from turtle import Turtle,Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)

tim.shape("arrow")
tim.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def circle(size_of_gap):
    gap = int(360 / int(size_of_gap))
    for i in range(gap):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + int(size_of_gap))

circle(5)



screen.exitonclick()