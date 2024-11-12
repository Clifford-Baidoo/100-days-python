from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=500,height=200)

def button_clicked():
    miles = float(input_label.get())
    km = miles * 1.609
    kilo_label.config(text=f"{km}")

#Equal to label 
equal_to_label = Label(text="is equal to")
equal_to_label.place(x=100, y=100)

#input
input_label = Entry(width=10)
input_label.place(x=200, y=70)
input_label.get()

#Kilo label
kilo_label = Label(text="0")
kilo_label.place(x=230, y=100)

#Calculate button
button = Button(text="Calculate", command=button_clicked)
button.place(x=200, y=150)

#Miles label
miles_label = Label(text="Miles")
miles_label.place(x=300, y=70)

#Kilo label
kilo = Label(text="Km")
kilo.place(x=300, y=100)

window.mainloop()