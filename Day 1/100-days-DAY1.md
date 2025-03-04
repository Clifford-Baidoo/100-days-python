## Day 1 - Printing Commenting,Debugging,String Manipulation and Variables

```Python
print function
    outputs what is in the parenthesis
    print("Something")
    "" - They show the beginning and end of the characters
strings - pieces of text
```

### 005 - Band Name Generator

A program that will Generate a band name for a band
```Python
print("Welcome to the Band Name Generator.")
street = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + street + " " + pet)
```

### 006 - Print function
#Showing the use of the print function
```Python
print("Hello World!")
```

### 007 - Interactive Assignment
An Interactive Assignment

After you have written your code you should run your program and it should print the following
Day 1 - Python Print FUnction
The function is declared like this:
print('what to print)

Solution
```Python
print('Day 1 - Python Print Function')
print('The function is declared like this:')
print("print('what to print')")
```

### 008 - String Manipulation and Code Intelligence
\n - to create a new line in the print function
print("Hello World!\nHello world!")

Concatenation
Combining different strings so they would be added to different strings
```Python
print("Hello" + "Angela")
    output = HelloAngela

print("Hello" + " " + "Angela")
    output = Hello Angela
```


### 009 - Interactive Assignment 2
Fix the code below
```Python
print(Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
    print('e.g. print("Hello" + "world")')
print(("New lines can be created with a backslash and n."))
```
#solution
```Python
print("Day 1 - String Manipulation")
print("String Concatenation is done with the '+' sign.")
print('e.g. print("Hello" + "world")')
print("New lines can be created with a backslash and n.")
```

### 010 - The input function
Input - Allows users to enter some data into the program
```Python
input("What is your name?")
print("Hello" + input("What is your name?"))
    output = Hello [name entered]
```

### 011 - Interactive Assignment 3
#Input Assignment
#print the number of elements in the string after the user inputs hwan hwan

#solution
```Python
print(len(input("Enter a name: ")))
    input:Clifford
    output:8
```

### 012 - Python Variables
Variables - A symbolic name that is reference or pointer to an objects

```Python
name = "Jack"
#name is the variable
print(name)

name = "Angela"
print(name)

name = input("What is your name?")
length = len(name)

print(length)

013 - Interactive Assignment 4
#Write a program that switches the values stored in the variables a and b

a = input("a: ")
b = input("b: ")

###########################
c = a
a = b
b = c

print(a)
print(b)



###########################

print("a = " + a)
print("b = " + b)
```

### 014 - Variable Naming
Naming variables is very crucial
Code must be readable

1.name of a variable has to be together
    user name=Kojo(wrong)
    user_name=Kojo(correct)
2.numbers can't be at the beginning of the name
    1user_name=Kojo(wrong)
    user_name=Kojo(correct)
3.names of functions cannot be used
    print=Kwesi(wrong)

015 - Project_Band Name Generator
#1. Create a greeting for your program
print("Welcome to BandGen")

#2. Ask the user for city that they grew up in
city = input("Enter the name of the city you grew up in:\n")

#3. Ask the user for the name of a pet
pet = input("Enter the name of your pet:\n")

#4. Combine the name of their city and pet and show them their band name
bandname = city + " " + pet
print(bandname)

#5. Make sure the input cursor shows on a new line
