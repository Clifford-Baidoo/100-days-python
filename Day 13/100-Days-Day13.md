## Day 13 - Debugging

### 122 - Describe the Problem
Debugging in Python refers to the process of identifying and fixing errors or bugs in the code.

To get started look at the function describe the problem and see what is wrong with it
For this function it is having a problem with the range cause it will be 1 to 19 instead of 20 and i == 20 which means the if statement won't work
Fix this in your own code or check my code to see how I fixed it

```Python
############DEBUGGING#####################

#Describe Problem
 def my_function():
   for i in range(1, 20):
     if i == 20:
       print("You got it")
 my_function()
```
To get started look at the function describe the problem and see what is wrong with it
For this function it is having a problem with the range cause it will be 1 to 19 instead of 20 and i == 20 which means the if statement won't work
Fix this in your own code or check my code to see how I fixed it

### 123 - Reproduce the Bug
The next step is to think about reproducing the bug , because if you Reproduce it you get to know how it works and how to fix it
when you run this code sometimes it will work but occasinaly you will get an error
and you must reproduce it to see when it happens so you can fix it
so run the code till you get an error and see how to fix it
#Hint - It is something about the index
```Python
 # Reproduce the Bug
 from random import randint
 dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
 dice_num = randint(1, 6)
 print(dice_imgs[dice_num])
```


### 124 - Play Computer
Step 3 is to play Computer
Pretend to be the computer and think about what you will do on each line
Take a look at the code and play computer
what if year = 1994 or 1980 would you give an output?
what would you do
Use this to figure out what is wrong with the code

```Python
# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")
```
### 125 - Fix the Errors
The next step is to fix the errors sometimes the terminal or debugger will tell you what is wrong
but sometimes you have to run the code before you can see the error
in the code two errors are inside one will show itself as soon as you type it in your ide the other one won't show unless you type an input
use the previous steps and see if you can fix the errors
```Python
# Fix the Errors
age = input("How old are you?")
if age > 18:
print("You can drive at age {age}.")
```

### 126 - Print is Your Friend
Print is your best friend you can always rely on it to reveal what is wrong with your code
whenever you are facing an issue you can print some parrt of your code to reveal stuff that is wrong
for the code below try using print to see if you can fix the errors
```Python
#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
```

### 127 - Use a Debugger
A debugger is a tool or software that helps developers identify and fix errors in a program by allowing them to examine the program's execution in real time.
Copy the lines of code and put it in a debugger like thonny or pythontutor
it will show you how the code works step by step and also show you the error
```Python
#Use a Debugger
def mutate(a_list):
   b_list = []
   for item in a_list:
     new_item = item * 2
   b_list.append(new_item)
   print(b_list)

mutate([1,2,3,5,8,13])
```

### 128 - Final Tips
- Take a Break - Rest small and come back you will be surprised how much easy it will be after some rest

- Ask a Friend - Ask someone for help when you are stuck , remember two heads are better than one

- Run Often - Run your code often , don't wait until you have written bunch of codes before you run your code , run it after every little execution

- Ask StackOverflow - You can meet developers on StackOverflow who can help you with bugs you are facing

### 129 - Interactive Assignment 1
Debug Odd or Even

#### Instructions
Read this the code in main.py
- Spot the problems 🐞.
- Modify the code to fix the program.
- Fix the code so that it works and passes the tests when you submit.

#### Hint
Review the previous lesson and go through the 10 steps to tackle these debugging problems.

```Python
number = int(input("Which number do you want to check?"))

if number % 2 = 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

```
### 130 - Interactive Assignment 2
Debug Leap Year
#### Instructions
Read this the code in main.py
- Spot the problems 🐞.
- Modify the code to fix the program.
- No shortcuts - don't copy-paste to replace the code entirely with a working solution.
- Fix the code so that it works and when you run it, it should pass all the tests.

```Python
year = input("Which year do you want to check?")

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

```

### 131 - Interactive Assignment 3
Debugging Fizz Buzz
#### Instructions
Read this the code in main.py
- Spot the problems 🐞.
- Modify the code to fix the program.
- No shortcuts - don't copy-paste to replace the code entirely with a working solution.
- The code needs to print the solution to the FizzBuzz game.
```
Your program should print each number from 1 to 100 in turn.

When the number is divisible by 3 then instead of printing the number it should print "Fizz".

When the number is divisible by 5, then instead of printing the number it should print "Buzz".

And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`
```
Hint
There is more than one fix required.

```Python
for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])
```

### 132 - Congratulations
You have completed day 13
Feels good huh




