'''Write a program that works out whether if a given year is a
leap year. A normal leap year has 366 days, with an extra
day in February.

This is how you work out whether if a particular year is a leap year

on every year that is evenly divisible by 4
except every year that is evenly divisible by 100
unless the year is also evenly divisible by 400

e.g The year 2000            e.g The year 2100
2000 / 4 = 500 (Leap)        2100 / 4 = 525 (Leap)
2000 / 100 = 20 (Not Leap)   2100 / 100 = 21 (Not Leap)
2000 / 400 = 5 (Leap)        2100 / 400 = 5.25 (Not Leap)
So 2000 is a Leap year       So 2100 is not a Leap year'''

#Don't Change the Code Below
year = int(input("Which year do you want to check? \n"))
#Don't Change the Code Above

#Write your code below this line
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year} is a Leap year")
        else:
            print(f"The year {year} is not a Leap year")
    else:
        print(f"The year {year} is a Leap year")
else:
    print(f"The year {year} is not a Leap year")