#Higher Lower game
from art import logo,vs
from data import info
import random

#def information():
#   for person in info:
#        print(f"Compare A: {person["name"]},{person["description"]},{person["country"]}")
print(logo)
person1 = random.choice(info)
person2 = random.choice(info)

print(f"Compare A: {person1["name"]},{person1["description"]},{person1["country"]}")
print(vs)

is_same = True
while is_same:
    if person1 == person2:
        person2 = random.choice(info)
    else:
        is_same = False
        print(f"Compare B: {person2["name"]},{person2["description"]},{person2["country"]}")

user_choice = input("Who has more Followers? A or B: ")

if user_choice == "A":
    user_value = person1["follower_count"]
    system_value = person2["follower_count"]
    print(user_value)
    print(system_value)

elif user_choice == "B":
    user_value = person2["follower_count"]
    system_value = person1["follower_count"]
    print(user_value)

else:
    print("Invalid input")

if user_value > system_value:
    print("You are correct!")
    print("You win")
else:
    print("You lose")

        
        

