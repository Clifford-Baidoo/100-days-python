#Love Calculator
'''You are going to write a program that tests the compatibility between two people.
We're going to use the super scientific method recommemded by BuzzFeed.

To work out the love score between two people:
    Take both people's names and check for the number of times the letters
    in the word TRUE occurs .Then check for the number of times the letters
    in the word LOVE occurs . the second name.Then combine these numbers to make a 2 digit number

For Love Scores less than 10 or greater than 90, the message should be:
    "Your score is x,you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:
    "Your score is y, you are alright together"

Otherwise, the message will just be their score. e.g.:
    "Your score is z"

Hint
1.The lower() function changes all the letters in a string to lower case
2.The count() function will give you the number of times a letter occurs in a string'''

# Don't change the code below
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
#Don't change the code above

#Write your code below the line

name1 = name1.lower()
name2 = name2.lower()

T=name1.count("t") + name2.count("t")
R=name1.count("r") + name2.count("r")
U=name1.count("u") + name2.count("u")
E=name1.count("e") + name2.count("e")

L=name1.count("l") + name2.count("l")
O=name1.count("o") + name2.count("o")
V=name1.count("v") + name2.count("v")
Z=name1.count("e") + name2.count("e")

digit_1=T + R + U + E
digit_2=L + 0 + V + Z

final_digit= int(str(digit_1)  + str(digit_2))

if final_digit < 10 or final_digit > 90:
    print(f"Your score is {final_digit},you go together like coke and mentos")
elif 40 >= final_digit <= 50 :
    print(f"Your score is {final_digit}, you are alright together")
else:
    print(f"Your score is {final_digit}")


