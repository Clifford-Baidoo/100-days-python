#if condition:
#    if another condition:
#       do this
#   else:
#        do this
#else:
#   do this

print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
    print("You can ride the rollercoastere!")
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12")
else:
    print("Sorry,you have to grow taller before you can ride.")


#if condition1:
#    do A
#elif condition2:
#    do B
#else:
#    do this

print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
    print("You can ride the rollercoastere!")
    if age < 12:
        print("Please pay $5.")
    elif 12 > age < 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry,you have to grow taller before you can ride.")