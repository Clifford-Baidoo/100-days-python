### Day 10 - Functions with Outputs

### 097 - Day 10 Goals
we are going to learn functions with outputs
and we are going to use it to build a calculator app

### 098 - More Functions
Functions with outputs allows output after the function has been called

```
def my_function():
    result = 3 * 2
    return result

my_function()
```
The return variable will return the output of the code to the user

```
#Functions with Outputs

def format_name(f_name,l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"

print(format_name("CliForD", "BaiDoo"))
```
This code will return the first and last name but will print the first letters as capital letters because of the title function

### 099 - Multiple Return Values
Return tells the computer that this is the end of the function so anything after return will not be acknowledged by the computer

You can use an early return for a function if there is no input for it

```
def format_name(f_name, l_name):
    if f_name =="" or l_name == "":
        return "You didn't provide valid inputs."
    def format_name(f_name,l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"Result: {formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))
```
### 100 - Days in Month Exercise
Instructions
In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.

You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.

days_in_month(year=2022, month=2)
And it will use this information to work out the number of days in the month, then return that as the output, e.g.:

28
The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.

Hint
Look at the function call at the bottom of the code to see the positional arguments. The order is very important.

Feel free to choose your own parameter names.

Remember that month_days is a List and Lists in Python start at position 0. So the number of days in January is month_days[0]

Be careful with indentation.

```
def is_leap(year):
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

def days_in_month():
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


#🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
```
#Solution
Check 100-interactivetest.py

### 101 - Doctstrings
Creating documentation while coding
So it is basically giving a guide about functions when coding
You can create it by typing "docstrings" on the first line after defining your function

```
def function1():
    '''This is a docstring'''
    a = "Clifford"
    record = print(a)
    return a

function()
```

You can use ''' for making multiline comments just make sure to end it with another '''
```
'''Blah Blah Blah
More Blah Blah'''
```

### 102 - Calculator Part 1

Instructions

First create a function for adding
```
def add(n1,n2):
    return n1 + n2
```
Do same for the other operations

create a dictionary where the keys are the symbols of the operators and the values are the names of the functions

Create a variable called num1 for input and do same for num2

Create a for loop that will loop through the dictionary and print all the operators and ask the user to select one

Now pick out the value of the operator and make it use the function to calculate the two numbers

#Solution
check 102-calculatorstart.py


### Print vs Return


In Python, `print` and `return` are used for different purposes in a function or script. Here's a comparison of the two:

---

##### 1. **`print()`**:
- **Purpose**: The `print()` function outputs a message to the console or terminal. It is primarily used for displaying information to the user.
- **Use Case**: It is typically used for debugging or showing results during the execution of a program.
- **Effect**: It does not affect the flow of the program or provide any value back to the caller. It simply sends text to standard output (the screen).
- **Example**:
  ```python
  def greet():
      print("Hello, World!")  # This will print the message to the console
  greet()  # Output: Hello, World!
```

The `return` statement in Python is used inside a function to pass a value back to the caller. It is a crucial aspect of function control flow and allows for further use of the function's result. Here's a detailed breakdown of how `return` works:

---

##### **Purpose**:
- The `return` statement stops the execution of the function and optionally provides a value that the caller can use.
- It allows the result of a function to be used in other parts of the program.

---

#### **Use Case**:
- You use `return` when you want to obtain a value from a function and use it for further computations or storage.
- This is commonly used in mathematical functions, data processing, and other operations that require a result to be returned.

---

#### **Effect**:
- When `return` is executed, the function is exited immediately, and the value (if provided) is sent back to the point where the function was called.
- Any code after the `return` statement in the function is not executed.

---

#### **Example**:
```python
def square(x):
    return x * x  # The result is sent back to the caller

result = square(4)  # The returned value is assigned to 'result'
print(result)  # Output: 16
```

### 104 - While Loops,Flags and Recursion
We are going to continue our code by allowing a user to add  another calculation after finishing the first one
Or make it start a new calculation
or make it end

We use something called Recursion
which is calling a function in a function

[Use this Link to learn about Recursion](https://www.geeksforgeeks.org/recursion-in-python/)

#Solution
Check 104-whileloops.py for solution
please go through and see how I did it

### 105 - Calculator Finishing tactics
Import the logo from the art module in the folder art.py
Let the program accept floating points

#Solution
Check 105-calculate.py for solution

### 106 - Congratulations
You finished day 10
Wawolo
