## Day 16 - Object Oriented Programming(OOP)

### 144 - Why do we need OOP and how does it work
Object Oriented Programming
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects."
These objects are instances of classes and represent entities that can contain both data (attributes) and functions (methods).
The core principles of OOP are designed to improve the structure and organization of code, making it more modular, reusable, and easier to maintain.

### 145 - How to use OOP_ Classes and Objects
Object Oriented trys to model a real world object
In order to model a real world object e.g A waiter
we take two things into consideration
what it has and what it does

For a waiter
```
has = attributes: is_hold_plater = True
                  tables_responsible = [4,5,6]

does = methods: def take_order(table, order)
                    #takes order to chef
                def take_payment(amount):
                    #add money to restaurant
```
so what the object has is called attributes and what the object does is called methods
The attribute is a variable that is associated with a model object
Methods are just functions that a particular modeled object can do

An object is just a way of combining some piece of data and functionality all together in the same thing
We can have multiple objects generatedfrom the same objects
e.g Waiter
Waiter is the general object which multiple objects are generated from and it is called a class
Henry and Betty can be objects in that class

### 146 - Constructing Objects and Accessing their Attributes and Methods

```
Object       Class
car    = CarBlueprint()
```
In this code the object car is calling the class CarBlueprint

```Python
from turtle import Turtle
timmy = Turtle()
print(timmy)
```

we are going to use the Turtle module which is an exiting module in python
so the timmy object is calling the Turle class to print something from it

#### Object Attributes
To call on an attribute you have to type the name of the object and add a dot and add the attribute

```
car.speed
```

```Python
from turtle import Turtle,Screen
timmy = Turtle()
print(timmy)

my_screen = Screen()
print(my_screen.canvheight)
```
In this code we imported the screen class and called on an attribute called canvheight and used print to print out the output

#### Object Methods
For methods we do the same thing but the difference is that we bring a parenthesis after we type the method name

car.stop()
```Python
from turtle import Turtle,Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")

my_screen = Screen()
print(my_screen.canvheight)

my_screen.exitonclick()
```
In this code we added a shape() method to our code which will print out a turtle shape because we called on the method
and it does same for my_screen.exitonclick()

Turtle is a library we are using
if you want to know more about python you can check it by clicking on this [link](docs.python.org/3/library/turtle.html)

#### Challenge
Change the turtle color from default to any color and how to make it move forward by a hundred paces after reading the documentation

### 147 - Python Packages
A Python package is a collection of Python modules organized in a directory hierarchy.
A package allows you to organize and manage your code in a way that promotes reusability, modularity, and maintainability.

To use python modules you can go to [Pypi](pypi.org/search)
You can install it in your various IDEs
Search for pretty tables
we are going to use it to display tables
you can read through the documentation on this [site](code.google.com/archive/prettytable/wikis/Tutorial.wiki)

### 148 - Practice Modifying Object Atrributes and Calling Methods
```
from prettytable import PrettyTable
```
Check the documentation of PrettyTable
you will need it
Challenge 1 - Create an object under the pretty table class and name it as table

to add a column you use x.add_column("Name_of_Field","List of Data")
to delete a column you just replace the add with del
Challenge 2 - Add two colums to the table and give it any data you want

Object Attributes
You can change the style of the table by changing the attributes
You can use the attribute align to change the alignment of the table
align is the attribute for that and the options are "l","c" and "r"

Challenge 3 - Aligns the items in the list for it to be left aligned

#Solution
You can check the code to see the solution

### 149,150 - Building the Cofee Machine in OOP
We are going to make the Cofee Machine but we will OOP
If you follow the [replit link](https://repl.it/@appbrewery/oop-coffee-machine-start) you will find all the files required
You are to use the main.py only the other code is used as libraries
The documentation for the libraries will be added to the repo

### 151 - Congratulations
You have completed day 16
How do you feel
