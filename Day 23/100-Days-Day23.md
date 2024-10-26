## Day 23 - Capstone Project - Turtle Crossing Game

### 206 - Day 23 Goals
We are going to make a Turtle Crossing Game
We are going to use what we have learnt so far

Problem Break Down
1. Move the turtle with keypress
2. Create and move the cars
3. Detect Collision with car
4. Detect when turtle reaches the other side
5. Create a scorboard

### 207 - Starting Code
In the turtle-Starting-code folder you will find all the Starting code you need in the folder
Follow it and see if you can make the game

### 208 - How to use the Starting Code
In the main code all the classes from the other files have been imported
You need to figure out how you can implement the already writting code

### 209,210 - Step 1 and Step 2
In the folder you will find 2 files "209 Step 1 - Check out how the game play works.html"
and "210 Step 2 - Break down the problem.html"

Step 1 shows you how the game works 
Step 2 breaks down the problem for you so that you can start working 

### 211 - Move the Turtle
So to move the turtle who is our player
we will first go into the player class and inherit the Turtle class
then we will create a new turtle and set it heading to 90 degrees

then we will create two functions move_up and move_down()

after that we will go into the main function and let it detect our keys by using the onkey method

#Solution
Check the main.py and player.py for solution

### 212 - Create the Car Behaviour
You can create your car by going into the car_manager file and creating an empty list of cars
Then you Create a function in which you are going to create the car and add it to the cars list

Then you create a function which will move the car 
Figure out how you can make the cars generate slower

#Solution
Check car_manager.py for the solution

### 213 - Detect Collision
We add a for loop that runs through our all cars list in the main file
if the distance of the car to the player is less than 20 the game should end

#Solution
Check the Collision part of main.py

### 214 - Detect when the car has reached the other side
So first we will create a method in your player class for it to detect when it has reached the other side if it has it should return true
when that happens the turtle should go back to it starting point

the speed of the cars should also increase

#Check the codes for solution

### 215 - Create a Scoreboard
Create a Scoreboard that will change the level number to +1 after the player has crossed to the other side
when the player hits a car print game over

#Check scoreboard.py for solution

### 216 - Congratulations
You have completed day 23
See you next week
