from tkinter import *

window = Tk()
window.title("My First UI Program")
window.minsize(width=500,height=300)

#Label
my_label = Label(text="I Am a Label")
my_label.pack()


#Event Listener
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

#Button
button = Button(text="Click me", command=button_clicked)
button.pack()

#Input
input = Entry(width=10)
input.pack()
input.get()


window.mainloop()