#Odd or Even
#Write a program that works out whether if a given number
#is an odd or even number

#Even numbers can be divided by 2 with no remainder
#e.g. 86  is even because 86 / 2 = 43

#43 does not have any decimal places.Therefore the divison is clean
#e.g. 59 is odd because 59 / 2 = 36.875

number = int(input("Which number do you want to check: "))

if number % 2 == 0 :
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")