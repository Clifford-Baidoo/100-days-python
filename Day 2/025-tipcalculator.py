#Final Project
#Create a program that accepts the total bill , ask for the percentage of tip you want to give
#ask the number of people who want to split the bill and gives an amount that each person should pay

#Welcome message
print("Welcome to the tip Calculator")

#User input for the total bill
bill = float(input("What was the total bill? $"))

#User input for the percentage of tip
tip_percentage = float(input("What percentage tip would you like to give?10,12,or 15 : "))

#User input for the number of people
num_people = int(input("How many people to split the bill? "))

#Calculating the tip
tip = (bill * tip_percentage) / 100

#Calculating the total amount plus tip
total_amount = bill + tip

#Amount each person should pay
amount_per_person = total_amount / num_people

#Printing to user
#print(f"Each person should pay: ${round(amount_per_person,2)}")
print(f"Each person should pay: ${amount_per_person:.2f}")  #Using :.2f to make sure it will always give 2 decimal places