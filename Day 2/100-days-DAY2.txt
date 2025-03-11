Here's the raw Markdown code without the artifact formatting:

```markdown
# Day 2 - Data Types, Numbers, Operations, Type Conversion, f-strings

## 017 - Today's Project
After today, we will be able to build a "Tip Calculator Program".
It splits the bill between a group of people and also calculates the tip to be added.

- Welcome to the tip Calculator
- What was the total bill?
- How many people to split the bill?

## 018 - Python Primitive Data Types

**DATA TYPES** - Data types are classifications of various types of data that tell the interpreter how the programmer intends to use the data.

### 1. String
A string represents a sequence of characters.
"Hello", "Kofi", "Kwesi"

```python
print("Hello")
```

**Subscripting** - Pulling a particular character from a string
done by adding [] and putting the index of the character you want.

```python
print("Hello"[0])  # Output = H
```
(Programmers start counting from 0 so the first character will be 0)

```python
print("Hello"[4])  # Output = o
```

As long as a character is in a double quote it is a string.
Example - "123" = This is a string

```python
print("123"+"345")  # output - 123345
```

### 2. Integer (int)
Integers are whole numbers whether negative or positive.
12, 14, -15

```python
print(123 + 345)  # output - 468
```

### 3. Float Point Number (Float)
Floats are numbers that have a decimal place or point.
3.12, 45.3

```python
print(3.12)  # output - 3.12
```

### 4. Boolean (bool)
Boolean represents values True or False.
Both True and False have to begin with a capital letter.

```python
print(5>3)  # output - True
print(3>5)  # output - False
```

## 019 - Type Error, Type Checking and Type Conversion
Functions are blocks of reusable code that perform a specific type.

The `len()` function is used to return length (number of items) of an object.
```python
len("Hello")  # output - 5
len(4837)     # output - Type Error (because len doesn't support integers)
```

**Type Error**
A Type Error in Python occurs when an operation or function is applied to an object of an inappropriate data type.

```python
num_char = len(input("What is your name?"))
print("Your name has" + num_char + "characters.")
# output - TypeError: can only concatenate str (not "int") to str
```
We were concatenating a string to an integer which is not allowed.

**type() function** - Shows the data type you are working with.

```python
num_char = len(input("What is your name?"))
print(type(num_char))  # output - <class 'int'>
```

When working with a data type and you are not sure of what you are working with, you can use the `type()` function to check it.

**Type Conversion**
Changing a piece of data from one data type to another.

```python
num_char = len(input("What is your name?"))  # This is an integer
new_num_char = str(num_char)  # Change it to a string using str()
print("Your name has " + new_num_char + " characters.")
# output - Your name has 6 characters
```

Other Conversion examples:
```python
a = 123
print(type(a))  # output = <class 'int'>

a = str(123)
a = float(123)

print(70 + float("100.5"))
# the string "100.5" is converted to a float and is added to 70
# output - 170.5
```

## 020 - Interactive Assignment 1
Write a program that adds in a 2 digit number e.g if the input was 35, then the output should be 3+5 = 8

**Solution**
```python
number = input("Enter your 2 digit number:\n")
num1 = int(number[0])
num2 = int(number[1])
sum = num1 + num2
print(sum)
```
Check the actual code for a full explanation.

## 021 - Mathematical Operations
Mathematical operations in Python allow you to perform arithmetic computations.

**Operators**
- 3 + 5 - Addition
- 7 - 4 - Subtraction
- 3 * 2 - Multiplication
- 6 / 3 - Division
- 2 ** 2 - Exponent

Python uses **PEMDAS** to prioritize operators in one line:
- Parentheses ()
- Exponents **
- Multiplication *
- Division /
- Addition +
- Subtraction -

Calculation that is most to the left is prioritized.

```python
print(3 * 3 + 3 / 3 - 3)  # output - 7
print(3 * (3 + 3) / 3 - 3)  # output - 3
```

## 022 - Interactive Assignment 2
BMI Calculator Exercise
Write a program that calculates the Body Mass Index(BMI) from a user's weight and height.
BMI = weight(kg)/height**2(m**2)

Check the code for solution.

## 023 - Number Manipulation and F Strings
**Round() function**
Used to round off numbers or floats.
```python
print(round(8/3))
```

Adding `,` [number] allows it to round it off to the number of decimal places.
```python
print(round(8/3, 2))  # Rounds it off to two decimal places
print(round(2.666666, 2))
```

**Floor division**
Turns the output to an integer instead of a float.
Instead of using just one `/` you use `//`.
```python
print(8//3)  # output 2
print(type(8//3))  # output <class 'int'>
```

**Continue performing calculations on a variable**
```python
result = 4 / 2
result /= 2
print(result)  # output - 1

score = 0
# user scores a point
score += 1
print(score)  # output - 1

# user loses a point
score -= 1
print(score)  # output - 0
```
`[operator]=` adds, divides, subtracts or multiplies another value to the variable that has already been calculated.

**F-strings**
f-strings (formatted string literals) in Python are a way to embed expressions inside string literals, using curly braces {}.

```python
score = 0
height = 1.8
isWinning = True

# normally if we concatenate it won't work because they are different data types and we will get a type error

# to use, add an f in front of your string and put other data types in curly braces
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
```

## 024 - Interactive Assignment 3
Life In Weeks
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
"You have x days, y weeks, and z months left"
where x, y, and z are replaced with the actual calculated numbers.

Solution is in 024-Interactivetest3.py so check it out.

## 025 - DAY 2 - Project: TIP Calculator
Create a program that accepts the total bill, asks for the percentage of tip you want to give, asks the number of people who want to split the bill, and gives an amount that each person should pay.

**Output**
```
Welcome to the tip calculator
What was the total bill? [User Input]
What percentage tip would you like to give? 10, 12 or 15? [User Input]
How many people to split the bill? [User Input]
Each person should pay: [Amount Calculated]
```

Check 025-tipcalculator.py for answer.

## 026 - You are already in the top 50
You can do it.
Keep going.
Rest small.
See you tomorrow lads.
```