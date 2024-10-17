## Day 18 - Turtle Graphics,Tuples and Importing Modules

### 163 - Day 18 Goals
We will write a code that will generate million dollar pieces of odd work
We will use python turtle to generate beautiful dot paintings

### 164 - Understanding Turtle Graphics

It is a graphical library that allows you to create pictures and shapes by controlling a "turtle" (which acts as a cursor) on a virtual canvas. The turtle starts at a default position in the middle of the screen, and you can give it commands to move, turn, and draw lines.

To get started with Turtle you must read the [documentation](https://docs.python.org/3/library/turtle.html) and it will show you all the stuff you can do with Turtle

For this day we are going to work with the documentation a lot so you will need to read it
```Python
from turtle import Turtle,Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)


screen = Screen()
screen.exitonclick()
```
You can run this code and see how Turtle works
Once you read the documentation you will understand how it works

### 165 - Turtle Challenge 1
Draw a Square
- Draw a simple 100 x 100 square using turtle

#Solution
Check 165-turtle.py

### 166 - Importing Modules,Installing Packages and Working with Aliases

- Basic Import
This is the simplest and most common way to import an entire module. You will need to prefix any functions or variables with the module name.
```
Keyword   Module 
   |        |
   |        |
Import    turtle
```
- From import
Instead of importing the whole module, you can import specific functions, classes, or variables. This allows you to use the imported components directly without prefixing them with the module name.

```
keyword module_name keyword thing_in_module
   |        |         |           |
   |        |         |           |
from      turtle    import     Turtle
```

- Import All
This imports everything from a module into the current namespace. It can be convenient but can lead to namespace conflicts if multiple modules have functions with the same name.


```
keyword module_name keyword thing_in_module
   |        |         |           |
   |        |         |           |
from      turtle    import        *
```

- Aliasing Modules
You can create an alias for a module to make it easier to reference, especially for long module names or when you want to avoid naming conflicts.
```
Keyword   Module  Keyword  alias_name
   |        |        |          |
   |        |        |          |
Import    turtle    as          t
```
- Installing Modules
Installing modules in Python is essential for adding additional functionality to your programs. Python's package manager, pip, is the most common tool used to install and manage modules.

Python doesn't come with every module so you need to install them
and you can use pip to do that

so we will install a package called heroes
```Python
pip install heroes
```

### 167 - Turtle Challenge 2
- Draw a dashed line for 10 paces and will leave a gap of 10 paces and draw a solid line for 10 paces 
- Let it do this 20 times

#Solution
Solution is in 167-turtle2.py

### 168 - Turtle Challenge 3
- Draw a triangle , square , pentagon, hexagon , heptagon , octagon , nanogon and decagon

#Solution
Check 168-turtle3.py

### 169 - Turtle Challenge 4
- Program your turtle to create a random walk which changes colors every time 

### 170 - Python Tuples and How to Generate Random RGB Colors
A tuple in Python is an immutable, ordered collection of elements. It is similar to a list, but once a tuple is created, its elements cannot be modified (hence, immutable). Tuples are often used to group related pieces of data.

Tuples are created by placing values inside parentheses () and separating them with commas.

```Python
# Tuple with different data types
my_tuple = (1, "Hello", 3.14, True)

# Tuple of numbers
numbers = (10, 20, 30)

# Empty tuple
empty_tuple = ()
```
To use Random RGB Colors you have to change the colormode for it to accept rgb colors
```Python
t.colormode(255)

def random_color()
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
```

Challenge
- return the rgb values in a tuple and use it to generate a random color

### 171 - Turtle Challenge 5
- Make the turtle draw a number of circles each with a radius of 100 in distance

#Hint
Check the documentation 

#Solution
Check 171-turtle5.py for solution

### 172 - The Hirst Painting Project 1
Challenge
- Go to [Pypi](pypi.org) and search for colourgram install it and use it go extract rgb values from a hirst spot Painting (You can find one on google)

### 173 - The Hirst Painting Project 1
Challenge
Use Turtle to paint a hirst spot painting
- Pain it by 10 Rows of Space
- Each of the dots must be 20 in size

### 174 - Congratulations
You have completed Day 18
Congratulations
