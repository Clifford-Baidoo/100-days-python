## Day 9 - Dictionaries & Nesting

### 089 - Day 9 Goals
We are going to learn how to use dictionaries and nesting
At the end of the day we will make an auction program

### 090 - Dictionaries
 dictionaries are a data type that stores key-value pairs. A dictionary allows you to associate a value with a unique key, making it useful for situations where you need to quickly retrieve data based on a unique identifier.

 The key goes first follwed by the value
 ```
 {"Key":"Value"}
 {"Bug":"An error in a program that prevents the program from running as expected"}
 ```
 To add more values to the dictionary you just have to add comma and give a new key and value
 ```
 programming_dictory = {
 "Bug":"An error in a program that prevents the program from running as expected",
 "Function":"A piece of code that you can easily call over and over again",
 "Loop":"The action of doing something over and over again"
 }
 ```

 To retrieve an item from a dictionary you type the dictionary name with a square bracket and you type the key in the square bracket

 ```
 print(programming_dictory["Bug"])
 ```
Make sure to spell the key correctly or else there will be a key error


Adding new items to a dictionary
You can add a new item to a dictionary by typing the dictionary name,puting the new key in a square bracket and Entering the value

```
programming_dictory["Loop"] = "The action of doing something over and over again."
print(programming_dictory)
```

Creating an empty dictionary
You can do that by entering the dictionary name and giving it an empty curly bracket
```
empty_dictionary = {}
```

Wipe an existing dictionary
You use the same method as creating an empty dictionary but you use the name of an existing dictionary

```
programming_dictory = {}
print(programming_dictory)
```

Editing an item in a dictionary
Just change the value of the key that's it
```
programming_dictory["Bug"] = "A moth in my computer"
print(programming_dictory)
```

Looping through a dictionary
It is basically like how we loop through lists but if we just ask normally it will give us the key so we have to type the dictionary name and the key

```
for key in programming_dictory:
    print(key)
    print(programming_dictory[key])
```

### 091 - Interactive Assignment 1
Grading Program

Instructions
You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.

Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.

DO NOT modify lines 1-7 to change the existing student_scores dictionary.

DO NOT write any print statements.

This is the scoring criteria:

Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail"

Expected Output
'{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'

```
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.


#TODO-2: Write your code below to add the grades to student_grades.👇



# 🚨 Don't change the code below 👇
print(student_grades)
```
#Solution
Check 091-interactivetest.py

### 92 - Nesting
Nesting is storing or puting a list or a dictionary in another dictionary

```
{
Key: [List],
Key2: {Dict};
}
```

```
capitals = {
  "France":"Paris",
  "Germany":"Berlin",
}
```
```
#Nesting a List in a dictionary
travel_log = {
  "France": ["Paris","Lille","Dijon"],
  "Germany": ["Berlin","Hamburg","Stuttgart"]
}
```
```
#Nesting a list in a list
list = ["A","B",["a","b","c"],"D"]
```
```
#Nesting a dictionary in a dictionary
travel_log = {
  "France": {"cities_visited":["Paris","Lille","Dijon"],"total_visits:12"},
  "Germany": ["Berlin","Hamburg","Stuttgart"]
}
```
```
#Nesting a dictionary in a list
travel_log = [
  {
  "Country":"France",
  "cities_visited":["Paris","Lille","Dijon"],
  "total_visits":12
  }
  {
  "Country":"Germany",
  "cities_visited":["Berlin","Hamburg","Stuttgart"],
  "total_visits":5}
]
```
Now we have nested a list in a dictionary which is nest in a dictionary which is nested in a dictionary which is nested in a list


### 093 - Interactive Test 2
Dictionary in List

Instruction
Instructions
You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.

Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
You've visited Russia 2 times.

You've been to Moscow and Saint Petersburg.

DO NOT modify the travel_log directly. You need to create a function that modifies it.

Hint
Look at the function call above to see what the name of the function should be.

The inputs for the function are positional arguments. The order is very important.

Feel free to choose your own parameter names.

#Solution
Check 093-interactivetest.py for solution


### 094 - The Secret Auction Program Instructions
Instruction
The objective is to write a program that will collect the names and bids of different people. The program should ask for each bidder's name and their bid individually.

Welcome to the secret auction program.
What is your name?: Angela
What's your bid?: $123
Are there any other bidders? Type 'yes' or 'no'.
yes
If there are other bidders, the screen should clear, so you can pass your phone to the next person. If there are no more bidders, then the program should display the name of the winner and their winning bid.

The winner is Elon with a bid of $55000000000
Use your knowledge of Python dictionaries and loops to solve this challenge.

```
from replit import clear
#HINT: You can call clear() to clear the output in the console.
```

### 095 - Solution
You know the drill
Check 095-aunctionsolution.py for answer

### 096 - Congratulations
You survived
Wowzers
Day 9 done
