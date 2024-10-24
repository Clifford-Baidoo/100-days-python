## Day 22 - The Pong Game

### 196 - Day 22
We are going yo create a pong game

#BreakDown the problem
1. Create the screen
2. Create and move a paddle
3. Create another paddle
4. Create the ball and make it move
5. Detect Collision with ball and bounce
6. Detect Collision with paddle
7. Detect when the paddle misses
8. Keep Score

### 197 - Set up the Main Screen
#Challenge 
- Create a new file called main and set up the screen 
- It should have a height of 600 and a width of 600
- It should have a black background

#Solution
Check 197-main.py for solution

### 198 - Create a Paddle that responds to Key Presses
#Challenge
- Create a paddle that accepts key presses to move up and down 
- It should have a height of 100 and a width of 20
- It should have an x_position og 350 and a y_position of 0

#Hint
Check the documentation on how to use
the shape method
    color method
    shapesize method
    goto method
    listen method
    on key method

### 199 - Write the Paddle Class and Create the Second Paddle
We are going to create a new file called paddle.py and create a class

#Challenge
Change the old paddle code and make it into a class that will accpet a tuple so that you can create a left paddle and a right paddle

move the left paddle by using w and s and the right paddle by using up and down

#Solution is in the paddle.py

### 200 - Write the Ball Class and Make the Ball Move
#Challenge
Create a ball class in a new ball.py file
- The ball has to start in the middle
- It should move upwards after every refresh

#Solution
Check ball.py for solution 

### 201 - Add the Ball Bouncing Logic 

```Python
   self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
```
To make the ball bounce we will add a new method which will multiply the y axis with -1 

```python
if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce()
```
And what will happen is when the ball goes over 300 or -300 the bounce method will be initiated which will cause the y axis to change to negative and cause the ball to bounce back 

### 202 - How to Detect Collisions with the Paddle
To make it detect collision with the paddle we will tweak it with the bounce method

```Python
    def bounce_x(self):
        self.x_move *= -1
```

```Python
if ball.distance(r_paddle) and ball.xcor() > 320 or ball.distance(l_paddle) and ball.xcor() < - 320:
        ball.bounce_x()
```

It uses the same logic as the ball bouncing but this one works with the x axis anf the distance between the ball and the two paddles 

### 203 - How to Detect when the Ball goes Out of Bounds
Challenge
Detect if the ball goes out of bounds at the edge of the screen.
If yes, reset the ball's position to the center of the screen.The ball should then start moving towards the other player

#Solution
Check the main file for the solution and also check the ball.py for the solution

### 204 - Score Keeping and Changing the Ball Speed

```Python
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100,200)
        self.write(self.l_Score,align="center",font={"Courier",80,"normal"})
```
This line of code will display the first scoreboard on the left after it is called in the main.py file

#Challenge
Try doing the right side on your own and making it add scores and change speed once it hits a paddle

#Solution
Check the rest of the code to see how it was implemented

### 205 - Congratulations
Day 22 done
Congratulations
