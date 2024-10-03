## Day 6 - Functions,Code Blocks and While Loops

### 057 - Day 5 Goals
We will learn about code blocks and while loops
We are going to write a program that will make a robot complete any randomly generated maze

### 058 - Defining and Calling Python Functions
Functions are reusable blocks of code that perform a specific task

We have already used some functions
Examples are
- len()
- round()
- input()
- int()
- print()

Every function has a name followed by a set of parentheses
`print("Hello")`
`len("Hello")`
Whatever is in the function will be outputed depending on what the funtion does

What if we wanted to make our own functions
That is when definig comes in
To do that we use def which means defining and giving it a function name and after that a colon and you write what is should do

After defining your function it can't run on it own unless you call it by typing the name of the function and any input it requires

```
def my_function():
    #Do this
    #Then do this
    #Finally do this
my_function() - To call the funtion
```

```
def my_function():
    print("Hello")
    print("Bye")

   my_function()
```
Press on this link to test how to use functions to make a robot move
[Link to Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json)

You can use Reeborg's keyboard to see the functions there

Challenge - Let the robot turn right
Challenge2 - Make the robot draw a little square in 4 boxes
#Solution is in 058-def.py

### 059 - Interactive Assignment 1
Reeborg needs to move over the hurdles write a code that will allow him to do so
Go to the link below and solve the issue
[Link to Hurdles Challenge](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json)

#Check 059-Interactivetest1.py for solution

### 060 - Identation
Indentation refers to the spaces or tabs placed at the beginning of a line of code.

```def my_function():
       print("Hello")
```
Indentation is mostly done by 4 spaces or 1 tab
Indentation in python is mandatory

```
def my_function():
....if sky == "clear":
........print("blue")
....elif sky == "cloudy":
........print("grey")
....print("Hello")
```

Count the dots to see how Identation works


### 061 - While Loops
A While loop will continue to run while a particular condition is true

while something_is_true:
    #Do something repeatedly

first we have a while keyword and a condition to test
if it is true it will do what you put under it until it becomes false

Using the Hurdle 1 Challenge
instead of using a for loop we are going to use a while loop to run the code

```
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
```

#Challenge
Select hurdle 2 and check world info for the prompt and solve it
[Link for Hurdle 2](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json)

Check 061-whileloop.py for Solution

### 062 - Interactive Assignment 2
Hurdles Challenge using While Loops
Select Hurdle 3 and check world info for the prompt and solve it

[Link for Hurdle 3](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json)

### 063 - Interactive Assignment 3
Final Hurdle Challenge
Select Hurdle 3 and check world info for the prompt and solve it
[Link for Hurdle 4](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json)
Also check Reeborg keyboard to see the functions there

#Solution
Check 063-interactivetest.py for solution

### 064 - Final Project
Write some that allows the robot to navigate through the maze and to get to the goal

[Link for Maze](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)

#Solution
Check 064-maze.py for Solution

### 065 - Congratulations.py
Congratulations on completing the day
Yay
