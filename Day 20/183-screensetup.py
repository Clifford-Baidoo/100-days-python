#Import your tutle and screen class
from turtle import Turtle,Screen

#Setup your screen by giving it a height and width
screen = Screen()
screen.setup(width=600,height=600)
#Set background color and title using .bgcolor and .title("Name")
screen.bgcolor("black")
screen.title("My Snake Game")

x_positoins = [-0,-20,-40]
squares = []

for i in range(0,3):
     tim = Turtle(shape="square")
     tim.color("white")
     tim.penup()
     tim.goto(x=x_positoins[i],y=0)
     squares.append(tim)




#Set the screen to only close if it is clicked on 
screen.exitonclick()