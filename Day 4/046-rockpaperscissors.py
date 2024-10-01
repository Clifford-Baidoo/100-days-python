#Create a program that allows a user to play rock paper scissors with the computer
#the user inputs their choice and depending on that choice the user either wins loses or draws

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

choice = int(user_choice)

choice_list=[0,1,2]
komputa_choice = random.choice(choice_list) 

if choice == 0 and komputa_choice == 0:
    print(f"You chose : \n {rock} \n Computer chose: \n {rock} \nIt is a draw")

elif choice == 1 and komputa_choice == 1:
    print(f"You chose : \n {paper} \n Computer chose: \n {paper}\nIt is a draw")

elif choice == 2 and komputa_choice == 2:
    print(f"You chose : \n {scissors} \n Computer chose: \n {scissors}\nIt is a draw")

elif choice == 0 and komputa_choice == 1:
    print(f"You chose : \n {rock} \n Computer chose : \n {paper}\n Computer wins")

elif choice == 0 and komputa_choice == 2:
    print(f"You chose : \n {rock} \n Computer chose : \n {scissors}\n You win")

elif choice == 1 and komputa_choice == 2:
    print(f"You chose : \n {paper} \n Computer chose : \n {scissors}\n Computer wins")

elif choice == 1 and komputa_choice == 0:
    print(f"You chose : \n {paper} \n Computer chose : \n {rock}\n You win")

elif choice == 2 and komputa_choice == 0:
    print(f"You chose : \n {scissors} \n Computer chose : \n {rock}\n Computer wins")

elif choice == 2 and komputa_choice == 1:
    print(f"You chose : \n {scissors} \n Computer chose : \n {paper}\n You win")

else:
    print("Enter a valid number")