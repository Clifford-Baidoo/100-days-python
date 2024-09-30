#Banker Roulette - Who will pay the bill
'''You are going to write a program which will select a random name from a list of names.
The person selected will have to pay for everybody's food bill'''

#Do not change the code below
import random

#Split string method
names_string = input("Give me everybody's names,seperated by a comma. ")
names = names_string.split(",")
#Do not change the code above

#Write your code below
random_name = random.choice(names)
print(f"{random_name} is going to buy the meal today!")

#The split() function helps convert data types into a list by using on identifier like (,)
