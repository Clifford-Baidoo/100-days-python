## Day 19 - More Turtle Graphics,Event Listeners,State and Multiple Instances

### 175 - Day 19 Goals
We are going to make an etch A Sketch Game that is going to allow us to use the up and down arrows to move our turtle forwads and back and we can turn our tutle clockwise and anticlockwise

We will also make a turtle racing game
The user will be able to place a bet and we will see who will win the race

### 176 - Python Higher Order Functions & Event Listeners
We need a way of listening to things the user does and the thing that allows us to that is called an event Listeners

if you look through the turtle doumentation you will see section for event Listeners

```Python
from turtle import Turtle,Screen
tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

screen.listen()
screen.onkey(key="space",fun=move_forwards)
screen.exitonclick()
```

In this code we defined a function called move forward which will move tim 10 paces 
and to use an even listener we will use screen.listen and screen.onkey
If you look through the documentation you will see that screen.onkey()takes two arguments
The key that the user will press on for it to activate and the function
And in this one we don't add a parenthesis to the function because it will be called when the user presses on the key

Functions as Inputs
```
def function_a(something):
    #Do this with something
    #Then do this
    #Finally do this
    
def function_b():
    #Do this
    
function_a(function_b)
```
Functions as Inputs is basically using other functions as inputs in another functions

A high order function is a function that can work with other functions
function_a is a Higher Order Function

### 177 - Challenge 1
Make an Etch-A-Sketch App
let W = Forwards
    S = Backwards
    A = Counter-Clockwise(Left)
    D = Clockwise(Right)
    C = Clear drawing
    
Let your turtle move in any of these directions according to the key pressed for it do draw anything you want to draw

### 178 - Object State and Instances


#### 1. **Instance**
An **instance** is an individual object created from a class. A class is like a blueprint, and an instance is a concrete realization of that blueprint.

- **Class**: Defines the structure and behavior (properties and methods) of objects.
- **Instance**: A specific object created from a class.

Each time you create an object from a class, you create an **instance**. For example, if you have a class `Car`, each individual car you create from this class is an instance.

##### Example:
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Create instances of the Car class
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.brand)  # Outputs: Toyota
print(car2.model)  # Outputs: Civic
```

#### Object State

The **state** of an object refers to the current values of its attributes (properties). The state of an object can change over time as its attributes are modified.

For example, if you have a class `Car`, the **state** of an instance of that class would be defined by the values assigned to its attributes, like `brand` and `model`.

##### Example:
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Create an instance of the Car class
car1 = Car("Toyota", "Corolla")

# Access the current state of car1
print(car1.brand)  # Outputs: Toyota
print(car1.model)  # Outputs: Corolla
```

### 179 - Understanding the Turtle Coordinate System

Imagine your screen has a height of 400 and a with of 500
then it means in the middle the Coordinate will be (0,0) but the height or y axis will be from 0 to 200 and 0 to -200 and the width or x axis will be 0 to 250 and 0 to -250


Challenge
Code will ask the user who will win the race
Once the user hits okay all the turtles will go to the starting point and be in different colors(6 colors for 6 turtles)


#Hint 
You can use screen.setup(width=number,height=number) to set up your screen dimension
You can use textinput to show a dialog window

### 180 - Aaaaand, we're off to the races
Please check the code to see how the completed code works

### 181 - You have completed Day 19
Day 19 done
Congratulations
Wohooo
