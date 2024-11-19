from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def gen_passwd():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_list = []

  password_letters = [choice(letters) for item in range(randint(8, 10))]
  password_symbols = [choice(symbols) for item in range(randint(2, 4))]
  password_numbers = [choice(numbers) for item in range(randint(2, 4))]

  password_list = password_letters + password_symbols + password_numbers
  shuffle(password_list)

  password = "".join(password_list)
  passwd_input.insert(0, password)

  pyperclip.copy(password)

  print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email = email_input.get()
    passwd = passwd_input.get()

    if len(website) == 0 or len(passwd) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        return
    else:
        is_ok = messagebox.askokcancel(title = website, message=f"These are the details entered: \nEmail: {email}" f"\nPassword: {passwd} \n Is it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {passwd}\n")
                website_input.delete(0,END)
                passwd_input.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="Day 29/262 password-manager-start/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website label and input
website = Label(text="Website:")
website.grid(row=1, column=0)

website_input = Entry(width=37)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

# Email/Username label and input
email = Label(text="Email/Username:")
email.grid(row=2, column=0)

email_input = Entry(width=37)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "baidooclifford56@email.com")

# Password label, input, and button
passwd = Label(text="Password:")
passwd.grid(row=3, column=0)

passwd_input = Entry(width=19)  # Adjust width for alignment
passwd_input.grid(row=3, column=1)

passwd_btn = Button(text="Generate Password",command=gen_passwd)
passwd_btn.grid(row=3, column=2)

# Add button
add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
