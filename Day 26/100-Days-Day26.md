## Day 26 - List and Dictionary Comprehensions

### 232 - Day Goals
By the end of the day we will build a NATO phonetics alphabet project

```Python
Enter a word: Angela
['Alfa','November','Golf','Echo','Lima','Alfa']
```
When we are done with the project this will be the output it will give use a list of NATO phonetics from the word we provide

### 233 - List Comprehension 
A list comprehension is a list you that you create from a an already existing list

we were already doing this with the for loop
#### For Loop
```Python
numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
```
How to Create a List Comprehension
You create the list in the same line with a set of brackets
then you add the parameters inside it

```Python
new_list = [new_item for item in list]
```

Using the first for loop to create a list comprehension
```Python
numbers = [1,2,3]
new_list = [n+1 for n in numbers]
```

#Challenge
Go into the Python console
then try creating a new list from numbers, where you added 1 to each value

You can also use a string to create a list comprehension
```Python
name = "Angela"
new_list = [letter for letter in name]
```
Run this code and see what happens

#Challenge 
Create a range (1,5) and loop through it to create a list comprehension where each of the numbers is doubled

#Conditional List Comprehension
This is where we add conditions so that if the condtion is true the list will be created
```Python
new_list = [new_item for item in list if test]
 ```

```Python
names = ['Alex','Caroline','Dave','Eleanor','Freddie']
short_names = [name for name in names if len(name) < 5]

print(short_names)
```
We used the if statement to see if the names in the list is shorter than 5 letters if yes the name will be added to the list

#Challenge
Create a new list that contains the names longer than 5 characters in all CAPS

### 234 - Interactive Exercise 1

#### List Comprehension 1
Instructions

You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain every number in the list numbers but each number should be squared.
'''
e.g. `4 * 4 = 16`
'''
4 squared equals 16.

DO NOT modify the List numbers directly. Try to use List Comprehension instead of a Loop.
Example Output
'''
[1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
'''
Hint

    Use the keyword method for starting the List comprehension and fill in the relevant parts.

    Make sure the squared_numbers is printed into the console for the code checking to work.

```Python
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:



#Write your code 👆 above:

print(squared_numbers)


```


The Solution is in 234-solution.py

### 235 - Interactive Exercise 2
#### List Comprehension 2
Instructions

You are going to write a List Comprehension to create a new list called result. This new list should only contain the even numbers from the list numbers.

DO NOT modify the List numbers directly. Try to use List Comprehension instead of a Loop.
Example Output
```
[2, 8, 34]
```
Hint

    Use the keyword method for starting the List comprehension and fill in the relevant parts.

    Even numbers can be divided by 2 with no remainder.

    Remind yourself of how the modulo operator works.

```Python
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:



#Write your code 👆 above:

print(result)


```

Solution is in 235-interactive2.py

### 236 - Interactive Exercise 3
#### List Comprehension 3

💪 This exercise is HARD
Instructions

Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

You are going to create a list called result which contains the numbers that are common in both files.

e.g. if file1.txt contained:
```
1

2

3
```
and file2.txt contained:
```
2

3

4

result = [2, 3]
```
IMPORTANT: The result should be a list that contains Integers, not Strings. Try to use List Comprehension instead of a Loop.
Example Output
```
[3, 6, 5, 33, 12, 7, 42, 13]
```
Hint

    Use the keyword method for starting the List comprehension and fill in the relevant parts.

    First, you will need to read from the files and create a list using the lines in the files.

    This method will be really useful: https://www.w3schools.com/python/ref_file_readlines.asp

    Remember you can check if a value exists in a list using the in keyword. https://www.w3schools.com/python/ref_keyword_in.asp

    Remember you can convert a string to an int using the int() method. https://www.w3schools.com/python/ref_func_int.asp


```Python


# Write your code above 👆

print(result)



```

Check 236-interactive3.py for solution

### 238 - Dictonary COmprehension
We are going to use dictionary comprehension

```Python
new_dict = {new_key:new_value for item in list}
```
It is the same as list comprehension but with a key and value

```Python
new_dict = {new_key:new_value for (key,value) in dict.items()}
```

This is to create a new dictionary from another dictionary

```Python
names = ['Alex','Beth','Caroline','Dave','Eleanor','Freddie']

students_sores = {student:random.randint(1,100) for student in names}
```
This code loops through the list and we create a random score to it

```Python
names = ['Alex','Beth','Caroline','Dave','Eleanor','Freddie']

students_sores = {student:random.randint(1,100) for student in names}

passed_students = {student:value for student:value in students_score if value > 80}
print(passed_students)
```

### 239 - Interactive Exercise 4
You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.

Try Googling to find out how to convert a sentence into a list of words.

Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.
Example Output
```
{

'What': 4,

'is': 2,

'the': 3,

'Airspeed': 8,

'Velocity': 8,

'of': 2,

'an': 2,

'Unladen': 7,

'Swallow?': 8

}
```
Hint

    Use the keyword method for starting the Dictionary comprehension and fill in the relevant parts.

    You can get a list of the words in a string by using the .split() method: https://www.w3schools.com/python/ref_string_split.asp

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:



print(result)

#Solution
Check 239-interactive4.py for solution

### 240 - Interactive Exercise 4
Dictionary Comprehension 2
Instructions

You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

To convert temp_c into temp_f:

(temp_c * 9/5) + 32 = temp_f

Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.
Example Output

{

'Monday': 53.6,

'Tuesday': 57.2,

'Wednesday': 59.0,

'Thursday': 57.2,

'Friday': 69.8,

'Saturday': 71.6,

'Sunday': 75.2

}

Hint

    Use the keyword method for starting the Dictionary comprehension and fill in the relevant parts.

    You can get each of the items from a dictionary using the .items() method: https://www.w3schools.com/python/ref_dictionary_items.asp

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:



print(weather_f)

### 241 - How to iterate over a Panda DataFrame

We aare going to to iterate over a dataframe
```Python
student_dict = {
    "student": ["Angela","James","Lily"]
    
}

student_data_frame = pandas.DataFrame(student_dict)

#Loop through a data frame
for (key, value) in student_data_frame.items():
    print(value)

#Panda has a built in loop which allows us to loop through the rows

for (index,row) in student_data_frame.iterrows():
    print(index)
    print(rows)
    print(row.student)
    print(row.scores)
```
We can use the itterows to loop through a panda dataframe which is better than using the normal for loop

### 242 - NATO Alphat Project
We are going to create a tool that takes the NATO phonetic alphabet and uses it to take input and prints the phonetics for that input

check 242NATO for the starting code
It has todo's that you can use as hints