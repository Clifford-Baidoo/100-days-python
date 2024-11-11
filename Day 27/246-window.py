import tkinter

window = tkinter.Tk()

#Change Title
window.title("My First GUI Program")

#Changing Size
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="I am a Label", font=("Arial",24,"bold"))
my_label.pack(side="left")

window.mainloop()