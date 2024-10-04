## Day 7 - Hangman Project

### 066 - Day 7 Goals
We are going to make a hangman game
Let's get started
We are going to use:
- for and while loops
- If/else statements
- Lists
- Strings
- Range
- Modules

### 067 - How to break a Complex Problem down into a Flow Chart

Flow Chart Programming
Drawing a flow chart to represent the logic of our game

Break it down into little steps

You can use [draw.io](https://draw.io) to create your flowchart


Check the flow chart to see how we are going to make the game

### 068 - Interactive Assignment 1
#### Picking Random Words and Checking Answers

```
#Step 1

word_list = ["ardvark","baboon","camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess.Make guess lowercase

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word
```

### 069 - Interactive Assignment 1 Solution
Check 069-interactivesolution1.py for solution

### 070 - Interactive Assignment 2
```
#Step 2

import random
word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)

#Testing Code
print(f"Psst, the solution is {chosen_word}")

#TODO-1 - Create an empty list called display.
#For each letter in the chosen_word,add a "_" to "display".
#So if the chosen_word was "apple",display should be ["_","_","_","_","_"] with 5 "_" representing each letter to guess.

guess = input("Guess a letter: ").lower()

#TODO-2 - Loop through each position in the chosen_word
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g If the user guessed "p" and the chosen word was "apple", then display should be ["_","p","p","_","_"].
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

#TODO-3 - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about the user to guess the next letter.We'll tackle that in step 3
```
### 071 - Interactive Assignment 2 solution
check 071-interactivesolution.py for answer

### 072 - Interactive Assignment 3
Checking if the Player has won

```
#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

guess = input("Guess a letter: ").lower()

#Check guessed letter
```
### 073 - Interactive Assignment 3 solution
check 073-interactivesolution.py for answer

### 074 - Interactive Assignment 4
```
#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1.
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
```
### 075 - Interactive Assignment 4 solution
Check 075-interactivesolution.py for solution

### 076 - Interactive Assignment 5
Final project
Improving the user Experience

```
#Step 5

import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
```

### 077 - Interactive Assignment 5 solution
Check 077-interactivesolution.py for solution

### 078 - Congratulations
You have completed day 7
Well done
