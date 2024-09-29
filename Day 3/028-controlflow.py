#if condition:
#   do this
#else:
#    do this

water_level = 50
if water_level > 80:
    print("Drain Water")
else:
    print("Continue")

#A program that uses if/else condition to do the work
#of a ticket box
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120: #required height for rollercoaster
    print("You can ride the rollercoaster") #indentation matters leave a required space
else:
    print("Sorry, you have to grow taller before you can ride")
