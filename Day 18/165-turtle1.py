from turtle import Turtle,Screen

tim = Turtle()
tim.shape("turtle")
tim.color("LawnGreen")

for i in range(4):
    tim.forward(100)
    tim.right(90)

screen = Screen()
screen.exitonclick()  # This will keep the window open until you click on it.  #