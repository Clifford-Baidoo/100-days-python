## Day 8 - Functions with inputs

### 079 - Day Goals
We will learn how to make functions take inputs
we will learn how to make Caeser Cipher

We will learn how to work with:
- Functions with inputs
- Arguments and Parameters

### 080 - Functions with Inputs

```
#Review:
#Create a function called greet()
def greet():
#Write 3 print statements inside the function.
    print("Hello Clifford,good day")
    print("How do you do Clifford")
    print("Isn't the weather nice today?")

greet
#Call the greet function and run your code

```

We are going to change the code for it to recieve inputs which will change the name everytime the code is run
That is functions with inputs

To do that we will add the name of our variable to the function to be able to call it

```
def my_funtion(variable)
    #Do this with variable
    #Then do this with variable
    #Finally do this with variable

my_function(Clifford)

```
After adding the data you want to input python will pass it over to the function
which will replace what is already there
so variable = Clifford

So make something in the first example to collect input
```
#Function that allows for input
def greet_with_name(name):
    print(f"Hello {name},good day")
    print(f"How do you do {name}")

greet_with_name("Clifford")
```
After the code is run the name will change to Clifford

```
   name = CLifford
    .       .
    .       .
    .       .
    .       .
Parameter  Argument
```

Parameter - The name of that data,it is used inside the function

Argument - the actual piece of data that is going to be passed over to the function when it's being called


### 081 - Positional vs Keyword Arguments

```
#Functions with more than 1 input
def greet_with(name, location)
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Clifford Baidoo", "Cape Coast")
```
Instead of just adding the Arguments we put them in quotations

##### Positional Arguments
Positional Arguments are arguments that need to be included in the proper position or order.
    So where you put them is where they are going to be passed over
    If you put Cape Coast on the first position name = Cape Coast

```
def my_function(a, b, c)
    #Do this with a
    #Then do this with b
    #Finally do this with c

my_function(1,2,3)
#a = 1 , b = 2  , c = 3

my_function(3,1,2)
#a = 3 , b = 1 , c = 2
```
This is how positional Arguments work

##### Keyword Arguments
Keyword arguments are a way to pass arguments to a function using named parameters.

```
def my_function(a, b, c)
    #Do this with a
    #Then do this with b
    #Finally do this with c

my_function(a=1,b=2,c=3)
#a = 1 , b = 2  , c = 3

my_function(c=3,a=1,b=2)
#a = 1 , b = 2 , c = 3
```
So for our original code use keyword arguments to call the arguments to the function instead of positional arguments


### 082 - Interactive Assignment 1
Paint Area Calculator

#Instruction
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height x wall width) ÷ coverage per can.


```
#Write your code below this line 👇







#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
```
#Solution
Check 082-interactivetest.py for solution

### 83 - Interactive Assignment 2
Prime number Checker

#Instructions
Prime numbers are numbers that can only be cleanly divided by itself and 1.

https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

```
#Write your code below this line 👇





#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)




```

#Solution
Check 083-interactivetest2.py for solution


### 084 - Caesar Cipher 1
if you don't know how Caesar Cipher works please use this link to find out
[Link to Cipher](https://cryptii.com/pipes/caesar-cipher)

We will start building the Caeser Cipher
When we type encode it should allow us to add a message and the shift number
When we type decode it should allow us to type our encoded message and add the shift number

```
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

```
#Solution
Check 084-caesar1.py for solution


### 085 - Caesar Cipher 2

Instruction
```
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text,shift_num):
    cipher_text = ""
    for i in plain_text:
            positon = alphabet.index(i)
            new_position = positon + shift_num
            new_text = alphabet[new_position]
            cipher_text += new_text

    print(f"The encoded text is {cipher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(plain_text,shift_num):
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
encrypt(plain_text=text, shift_num=shift)

```
#Solution
Check 085-caesar2.py for solution

### 086 - Caesar Cipher 3
```
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def encrypt(plain_text,shift_num):
    cipher_text = ""
    for i in plain_text:
            positon = alphabet.index(i)
            new_position = positon + shift_num
            new_text = alphabet[new_position]
            cipher_text += new_text

    print(f"The encoded text is {cipher_text}")

def decrypt(plain_text,shift_num):

  plain_txt = ""
  for i in plain_text:
       positon = alphabet.index(i)
       old_position = positon - shift_num
       old_text = alphabet[old_position]
       plain_txt += old_text

  print(f"The decoded text is {plain_txt} ")

if direction == "encode":
  encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
  decrypt(cipher_text=text, shift_amount=shift)
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
```

### 087 - Caesar Cipher 4

Instructions
```
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26.
#Hint: Think about how you can use the modulus (%).
def caesar(start_text,shift_num,cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
          shift_num *= -1
    for i in start_text:
       #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
       positon = alphabet.index(i)
       new_position = positon + shift_num
       end_text += alphabet[new_position]

    print(f"The {cipher_direction}d text is {end_text}")
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

caesar(start_text=text,shift_num=shift,cipher_direction=direction)
```
### 088 - Congratulations
You have finished day 8
Wowzers
