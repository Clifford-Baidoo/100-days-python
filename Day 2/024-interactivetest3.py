#Your Life In Weeks
#Create a program using maths and f-Strings that tells us how many,days,weeks,
#months we have left if we live until 90 years old
#It will take your current age as the input and output a message with our time left in this format:
#|You have x days,y weeks and z months left
#where x,y and z are replaced with the actual calculated numbers.

#1 year = 365 days
#1 year = 52 weeks
#1 year = 12 months

#Takes the age input
age = input("What is your current age?\n")

#subtract current age from 90 years
years_left = 90 - int(age)

#calculate days left
days_left = years_left * 365

#calculate weeks left
weeks_left = years_left * 52

#calculate months left
months_left = years_left * 12

print(f"You have {days_left} days, {weeks_left} weeks and {months_left} left.")
