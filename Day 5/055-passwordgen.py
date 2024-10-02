#Password generator
#Build a program that ask the user for the number of letters,numbers and symboles they want in the password and
#generate it for them

#Don't touch the code below
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#Don't touch the code above

#Write your code below
password=""

for char in range(1,nr_letters+1):
    random_char=random.choice(letters)
    password += random_char

for num in range(1,nr_numbers+1):
    random_num=random.choice(numbers)
    password += random_num
for symb in range(1,nr_symbols+1):
    random_symb=random.choice(symbols)
    password += random_symb

print(password)

#To Shuffle Password
list_password=list(password)
random.shuffle(list_password)

passwd = ""
for i in list_password:
    passwd += i

print(f"Your password is {passwd}") 



