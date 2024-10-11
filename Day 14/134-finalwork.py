from art import logo, vs
from data import info
import random

# Get a random person from the data
def get_persons():
    return random.choice(info)

# Format person's information for display
def format_persons(info):
    name = info["name"]
    description = info["description"]
    country = info["country"]
    return f"{name}, the {description}, from {country}"

# Check if the user's guess is correct
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Main game function
def game():
    print(logo)
    score = 0
    game_should_continue = True

    # Initialize the first two accounts
    a_account = get_persons()
    b_account = get_persons()

    # Continue the game until the player loses
    while game_should_continue:
        # Ensure that Account A and B are different
        while a_account == b_account:
            b_account = get_persons()
        
        print(f"Compare A: {format_persons(a_account)}")
        print(vs)
        print(f"Against B: {format_persons(b_account)}")

        # Ask for the player's guess
        guess = input("Who has more followers? Type 'A' or 'B':  ").lower()

        # Get follower counts for both accounts
        a_followers_check = a_account["follower_count"]
        b_followers_check = b_account["follower_count"]

        # Check if the guess is correct
        is_correct = check_answer(guess, a_followers_check, b_followers_check)

        print(logo)
        if is_correct:
            score += 1
            print(f"You are right! Current score: {score}")
            # Move B to A and get a new B for the next round
            a_account = b_account
            b_account = get_persons()
        else:
            print(f"You are wrong. Final score: {score}")
            game_should_continue = False  # End the game if the guess is wrong

# Start the game
game()
