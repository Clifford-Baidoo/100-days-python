#Import your tutle and screen class
from turtle import Turtle,Screen
import time  

#Setup your screen by giving it a height and width
screen = Screen()
screen.setup(width=600,height=600)
#Set background color and title using .bgcolor and .title("Name")
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)#Set's everything to 0 so there will be no animation until we call an update

x_positoins = [-0,-20,-40]
squares = []

for i in range(0,3):
     tim = Turtle(shape="square")
     tim.color("white")
     tim.penup()#This line stops a line from being drawn
     tim.goto(x=x_positoins[i],y=0)
     squares.append(tim)


#Creating a boolean variable and making a while loop
game_is_on = True
while game_is_on:
    screen.update()#Updates the screen animation to view the next slide instead of moving piece by piece
    time.sleep(0.1)#slows down the time
    
    for seg_num in range(len(squares) - 1,0,-1):#Create a for statement that uses the start stop and step which makes the for loop start from the first square instead of the last one
        new_x = squares[seg_num - 1].xcor() #sets a new x coordinate
        new_y = squares[seg_num - 1].ycor() #sets a new y coordinate
        squares[seg_num].goto(new_x,new_y)
    squares[0].forward(20)
    squares[0].left(90)

    
#Set the screen to only close if it is clicked on 
screen.exitonclick()