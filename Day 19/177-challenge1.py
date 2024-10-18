from turtle import Turtle,Screen
tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_clockwise():
    tim.right(10)

def move_anticlockwise():
    tim.left(10)

def clear():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=move_anticlockwise)
screen.onkey(key="d",fun=move_clockwise)
screen.onkey(key="c",fun=clear)

screen.exitonclick()