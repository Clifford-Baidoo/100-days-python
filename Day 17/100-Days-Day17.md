## Day 17 - Quiz Game

### 152 - Day 17 Goals
At the end of the day we will be able to make a quiz app with OOP
The user should be able to answer a question and the program is supposed to take scores of questions answered correctly

### 153 - How to create your own class
 The syntaz for creating a class is very simple
 you use the class keyword and you give it a name and the rest of the code will follow
```Python
 class Car:(and all the code in the class will follow)
```
```Python
class User:
    #Everything has to be indented after the colon
    pass#The pass variable is to tell python that the class or function should be empty


user_1 = User() #The Parenthesis is for initializing the class in the object
```

Every first letter of every word should be capitalized - Pascal Case

### 154 - Working with Attributes,Class Constructors
How to create an Attribute in a class
A Constructor is a part of the blueprint that allows us to specify what should happen when our object is being Constructed
It is also called initializing
we can make a Constructor using the init function and we use it to initialise attributes

```Python
class Car:
    def __init__(self):
    #initialise attributes
```
```Python
class Car:
    def __init__(self, seats):
        self.seats = seats
```
The init function is going to be called everytime we create a new object
The seats is an Attribute that has been created
so we can call it in an object instead of typing a new Attribute

```Python
class User:

    def __init__(self, user_id, username):
    self.id = user_id
    self.username = username

user_1 = User("001","Clifford")
#Now the values in the user_1 object will become the attributes for the class User
user_2 = User("002","Kingsley")
```

### 155 - Adding methods to the Class
lets say we have a method
def enter_race_mode():
    seats = 2

to add this to a class we put it under the class and use the attributes from the class

```Python
class Car:
    def enter_race_mode():
        self.seats = 2

my_car.enter_race_mode()
```
In this code we are using a method to get a car to enter race enter_race_mod
In which the car is an object my_car

A method always needs to have a self parameter so that when the object is called it will know what called it
```Python
class User:

    def __init__(self, user_id, username):
    self.id = user_id
    self.username = username
    self.followers = 0
    self.following = 0

    def follow(self,user)
        user.followers += 1
        self.following += 1

user_1 = User("001","Clifford")
#Now the values in the user_1 object will become the attributes for the class User
user_2 = User("002","Kingsley")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
```
now we have added a new method called follow which will allow the user to follow another user and when that happens the users followers remain the same but the following increases by 1

### 156 - Quiz Game Part 1
Create a Question with an __init()__ method with two attributes:question and answer

#Solution
Check 156-question_module.py for solution

### 157 - Quiz Game Part 2
Check the data.py file you will see bunch of questions and answers saved in a list called question_data
- Write a for loop to iterate over the question_data
- Create a Question object from each entry in question_data
- Append each Question object to the question_bank

### 158 - Quiz Game Part 3
- Create a class called QuizBrain
- Write an __init__() method
- initialise the question_number to 0
- initialise the question_list to an input

Once you are done with the first challenge
- Retrieve an item at the current question_number from the question_list
- Use the input() function to show the user the Question text and ask for the user's answer

### 159 - Quiz Game Part 4
- Create a method called still_has_questions()
- Return a boolean depending on the value of question_number'
- Use the while loop to show the next question until the end

### 160 - Quiz Project Part 5
- Create a method called check answer to check the answer to see if it is correct
- Add a new attribute called scores
- Let the method also inform users about their current score
- Let users see their final score after the quiz

### 161 - The Benefits of OOP
You can use the open trivia database to get new questions
[Link](opentdb.com)
Just Generate new questions and change the Key Value Pairs
Have fun

### 162 - Congratulations you have completed day 17
You have completed day 17
Congratulations


