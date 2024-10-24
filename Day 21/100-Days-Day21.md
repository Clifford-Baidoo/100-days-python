## Day 21 - Inheritance,slicing and finishing the snake game 

### 188 - Day 21 Goals
We are going to learn about inheritance and how to slice lists and dictionaries

### 189 - Class Inheritance
Class Inheritance is a process of inheriting behaviour and appearance from another class

You can inherit behaviour(method)
You can inherit appearance(attribute)

How inheritance works
To inherit a class you first declare your new class and add the name of the existing class in the parenthesis

To get all the attributes and methods from the class you use super().__init__()
What is does is initialize everything that the superclass animal can do in our fish


```Python
class Fish(Animal):
    def __init__(self):
        super().__init__()
```

```Python
class Animal:
    def __init__(self):
        self.num_eyes = 2
        
    def breathe(self):
        print("Inhale,exhale")
        
class Fish(Animal):
    super().__init__()
    
    def swim(self):
        print("movin in water")
        
nemo = Fish
nemo.swim
nemo.breathe
print(nemo.num_eyes) 
```

To make changes to a method in the inherited class you can just define the method and use the super class to call the method and add your changes to it

```Python
class Fish(Animal):
    def __init__(self):
        super().__init__()
```

```Python
class Animal:
    def __init__(self):
        self.num_eyes = 2
        
    def breathe(self):
        print("Inhale,exhale")
        
class Fish(Animal):
    super().__init__()
    
    def swim(self):
        print("movin in water")
        
    def breathe(self):
        super().breathe()
        print("Move underwater")
nemo = Fish
nemo.swim
nemo.breathe
print(nemo.num_eyes) 
```

### 190 - Detect Collisions with Food
What we are going to do is to make the food with is going to be a blue circle and anytime the snake touches it the food has to move to a new random location

We will create a new food.py file and make a class Food

Please check the code for all the codes


#Challenge
After creating your food class make it inherit the turtle class

```Python
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)
```        
We inherited the Turtle class and used it to set the shape of the food the size the color and the location it should be 

initialize the food class in the main.py file
Run the code and see what happens

we are going to detect collision in the main file under the while loop using the distance method
read the documentation to see what it does

```Python
if snake.head.distance(food) < 15:
    print("nom nom nom")
    
```
we will create a refresh method that will let the food go to a random location after it has collided with the snake
```Python
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)
```        

we will now add the method to the main.py file

```Python
if snake.head.distance(food) < 15:
    food.refresh()
    
```

### 191 - Create a Scoreboard and Keep Score
We are going to create a turtle that will act as a Scoreboard and it will stay in one place 

we are going to use the write method and clear method to do this
please check the documentation to see what it does

#Challenge
Create a new file called Scoreboard.py and create a class called Scoreboard
It is going to inherit from the turtle class
the Scoreboard is going to be a class that will display the score

#Solution
check the Scoreboard.py for the solution

### 192 - Detect Collisions with the Wall
We are going to write a code that will detect if the snake has crossed the boundary we are going to create

```Python
if snake.head.distance(food) < 15:
    food.refresh()
    scoreboard.increase_score()
    
if snake.head.xcor > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280: 
    game_is_on = False
```

#We will go into our scoreboard class and let it write game over once the snake goes out of bounds

```Python

def game_over(self):
    self.goto(0,0)
    self.write("GAME OVER",align=ALIGNMENT,font=FONT)
```
after you add this to your if statement anytime the snake goes out of bounds the program will end and write game over

### 193 - Detect Collisions with your own Tail
We have to extend the snake whenever it gets food so that it grows in length and we can detect collision

we will create an add_segment and extend method in our snake class
we will put the original code from the create_snake method into the add_segment class and we will call it in the create_snake method

and we will create a new if statement to check if the head is in the distance of any other part of the body if it is the game will end

#Code
Check snake.py for changes

### 194 - How to Slice Lists & Tuples in Python 
Slicing in Python

Slicing allows you to extract a portion of a sequence using the syntax:
sequence[start:end:step]

Basic slicing
```
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Slice from index 2 to 5 (excluding 5)
The element at index 2 is included, but index 5 is excluded.
```
print(my_list[2:5])  # Output: [2, 3, 4]
```

Omitting the start index will slice from the beginning of the list.
This extracts elements from the start to index 4 (5 is excluded).
```
print(my_list[:5])   # Output: [0, 1, 2, 3, 4]
```

Omitting the end index will slice from the start index to the end of the list.
```
print(my_list[5:])   # Output: [5, 6, 7, 8, 9]
```

You can use a step value to extract every nth element.
Here, we take every second element (step = 2).
```
print(my_list[::2])  # Output: [0, 2, 4, 6, 8]
```

Negative indices can be used to slice from the end of the list.
This extracts the last three elements.
```
print(my_list[-3:])  # Output: [7, 8, 9]
```

A step value of -1 reverses the list.
```
print(my_list[::-1])  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

### 195 - Congratulations
You have completed day 21
Congratulations
