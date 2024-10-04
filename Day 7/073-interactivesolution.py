#Step 3

import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

def loop():
    guess = input("Guess a letter: ").lower()

    for letter in chosen_word:
        if letter == guess:
            for i in range(word_length):
                if chosen_word[i] == guess:
                    display[i] = guess
    print(f"{' '.join(display)}")

while "_" in display:
    loop()
#Check guessed letter
print("You have won")