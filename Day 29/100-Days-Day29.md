## Day 29 - Building a Password manager 

### 261 - Day Goals
We are going to Generate a password manager that will store passwords for us or generate passwords for us

There is a zip file in the folder which contains a logo and a main.zip

### 263 - Challenge 1 - Creating the main screen
#Challenge
Display the logo with a width of 200 and a height of 200 with a padding of 20

HINT
Check the official documentation of [Canvas](effbot.org/tkinterbook/cavas.htm)


### 263 - Challenge 2 - Use grid() and columspan to complete the user interfacee
Columspan allows you to stretch a column into more rows

The interface we are creating is a three column and 5 row layout
the website and email/username has a width of 35
the password textarea has a width of 21 
the add button has a width of 36

### 265 - Challenge 3 - Saving Data to a File
Create a function that will save the user data to a file when the add button is clicked on

You can check the save password section if you are stuck

### 266 - Dialog Boxes and Pop-Ups in Tkinter
Standard Dialogs are popups that tkinter can generate

To generate dialogs you import message boxes 

```Python
from tkinter import messagebox

#inside def save()

messagebox.showinfo(title="Title",message="message")

mesagebox.askokcancel(title = website, message=f"These are the details entered: \nEmail: {email}" f"\nPassword: {password} \n Is it ok to save?")

if is_ok:
    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0,END)
        password_entry.delete(0,END)
```

#Challenge
Do not save the data and show the pop up above if the website or password fields were left empty


### 267 - Generate a Passowrd and Copy it to the Clipboard
In the folder you will find a code to the password generator code we made in day 5 copy it and put it in your code

Change the for loops to use List Comprehension instead
Remember to combine the results so that you can shuffle them to create a password

How to put strings into the clipboard
You can use pyperclip and use the .copy method

```Python
import pyperclip

pyperclip.copy("Message)
```