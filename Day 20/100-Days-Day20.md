## Day 20 - Building The Famous Snake Game

### 182 - Day 20 Goals
We will use the OOP and turtle model we have learnt to make to create the famous snake game 
The one that the snake goes after food and not hitting any walls

#### Breaking Down the Problem
We have 7 steps 
We will tackle the first 3 today and the remaining 4 tommorow

1. Create a snake body
2. Move the snake
3. Control the snake
4. Detect Collision with food
5. Create a scoreboard
6. Detect collision with wall
7. Detect collision with tail

### 183 - Screen Setup and Creating the Snake Body

#Setting up the Screen
```python
#Import your tutle and screen class
from turtle import Turtle,Screen

#Setup your screen by giving it a height and width
screen = Screen()
screen.setup(witdh=600,height=600)
#Set background color and title using .bgcolor and .title("Name")
screen.bgcolor("black")
screen.title("My Snake Game")




#Set the screen to only close if it is clicked on 
screen.exitonclick()
```

#### Task 1 - Create a snake body
A turtle has a dimension of 20 x 20 so if we want 3 of them lined up next to each other we have to think of their coordinate

#Challenge
Create 3 turtles and position them like so.
Each turtle should be a white square
```python
#Import your tutle and screen class
from turtle import Turtle,Screen

#Setup your screen by giving it a height and width
screen = Screen()
screen.setup(witdh=600,height=600)
#Set background color and title using .bgcolor and .title("Name")
screen.bgcolor("black")
screen.title("My Snake Game")

#You can type everything 1 by 1
segment_1 = Turtle(shape="square")
segment_1.color("white")
segment_1.goto(-20, 0)


segment_2 = Turtle(shape="square")
segment_2.color("white")
segment_2.goto(-20, 0)


segment_3 = Turtle(shape="square")
segment_3.color("white")
segment_3.goto(-20, 0)

#Or you can use a for loop to do that
x_positoins = [-0,-20,-40]
squares = []

for i in range(0,3):
     tim = Turtle(shape="square")
     tim.color("white")
     tim.goto(x=x_positoins[i],y=0)
     squares.append(tim)
     
#You can also use a different type of for loop
starting_positions = [(0,0) , (-20, 0) ,(-40, 0)]

for position in starting_positions;
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(position)
    
#Set the screen to only close if it is clicked on 
screen.exitonclick()
```
### 184 - Animating the Snake Segments on screen
In this part we are going to animate the snake segments

```python
#Import your tutle and screen class
from turtle import Turtle,Screen
import time  

#Setup your screen by giving it a height and width
screen = Screen()
screen.setup(witdh=600,height=600)
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
    for i in squares:
        i.forward(20)#for every index in the list that index should move 10 paces
#We will use the tracer method to stop the first animation of the squares moving into position
#Set the screen to only close if it is clicked on 
screen.exitonclick()
```
The code above moves the snake forward in a perfect animation but if you try to turn it then there will be a problem

The code below will show you how to fix that

```python
#Import your tutle and screen class
from turtle import Turtle,Screen
import time  

#Setup your screen by giving it a height and width
screen = Screen()
screen.setup(witdh=600,height=600)
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
        new_x = squares[seg_num - 1].ycor() #sets a new y coordinate
        segments[seg_num].goto(new_x,new_y)
    segment[0].forward(20)
    segment[0].left(90)

    
#Set the screen to only close if it is clicked on 
screen.exitonclick()
```

### 185 - Create a Snake Class & Move to OOP
We are basically going to make a snake class to tidy the code and put it in a file called snake.py so that it can be imported into another class

#Challenge
- Create a class called snake
- put the function that allows the snake to move in a method called move

#Solution
Check 185-main.py and snake.py for solution

### 186 - Control the Snake with a Keypress
We are going to get our code to listen to keypress for us to be able to control our snake

```python
from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

#To start listening for keystrokes
screen.listen()
screen.onkey(screen.up,"Up")
screen.onkey(screen.down,"Down")
screen.onkey(screen.left,"Left")
screen.onkey(screen.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
```
#Challenge 
- Create methods in the snake class that will allow the snake to go up,down,left and right whenever the keys are pressed
up = 90
down = 270
left = 180
right = 0 

- Make sure the snake is not able to move backwards
#Hint
You can use and if statement and a .heading() method for that

#Solution
Check snake.py for solution

### 187 - Congratulations
You have completed day 20
Congratulations
