'''You are going to write a program which will mark a spot with an X

The map is made of 3 rows of blank squares
     1    2     3
1 ['◻️','◻️','◻️']

2 ['◻️','◻️','◻️']

3 ['◻️','◻️','◻️']

Your program should allow you to enter the position of the treasure using a two-digit system.
The first digit is the horizontal column number and the second digit is the vertical row number.'''


#Don't change the code below
row1=["◻️","◻️","◻️"]
row2=["◻️","◻️","◻️"]
row3=["◻️","◻️","◻️"]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?")
#Don't change the code above

#Write your code below

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"

#Don't change the code below
print(f"{row1}\n{row2}\n{row3}")