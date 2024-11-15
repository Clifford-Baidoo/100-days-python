## Day 28 - Building a Pomodoro App

### 254 - Day Goals
The Pomodoro Technique  
1. Decide on the task to be done
2. Set the timer to 25 minutes
3. Work on the task until the timer rings
4. Take a short 5 minute break
5. Take a 15-30 minute break

We are going to build a timer with a tomato on it that will set at timer and when the timer is up it will prompt us that time is up
Just like the steps in the technique

### 254 How to work with Canvas Widgeat and add images to Tkinter
In the files you will see a starting zip file that contains all you need to start the project
Open the folder to get the image and the main file 

The instructions have been broken into sections which we are going to use

The first thing to do is to setup or UI
```Python
from tkinter import *

window = Tk()
window.title("Pomodoro")

window.mainloop()
```

Putting an image into the program
To put images into tkinter we are going to use the Canvas widget
```Python
from tkinter import *

window = Tk()
window.title("Pomodoro")
window.config(pdx=100,pdy=50)

canvas = Canvas(width=200,height=224)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(x=(103),y=112,image=tomato_img)
canvas.pack()

window.mainloop()
```
First we call the Cnavas widget and we set the width and height of the canvas and we use PhotoImage to search for the tomato.png and we use that in the canvas.create_image()

Displaying some text
```Python
from tkinter import *

window = Tk()
window.title("Pomodoro")
window.config(pdx=100,pdy=50,bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(x=(100),y=112,image=tomato_img)

canvas.create_text(100,130,text="00:00", fill="white",fonT=(FONT_NAME,35,"bold"))

canvas.pack()

window.mainloop()
```

### 256 - Challenge - Complete the Application's User Interface
Add a start and reset button to the buttom of the tomato and add a big Timer text on top of the tomato an also a checkmark betwwen the start and reset

Hint 1: use fg to color the Foreground 
Hint 2: Copy-Paste the Checkmark symbol
Hint 3: use grid() instead of pack()

check the main code for solution

### 257 - Adding a Count Down Mechanism
We will create a method in the countdown section

```Python
import math

#Timer section
def start_timer():
    count_down(5)

#Count down section
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000,count_down,count - 1)

#In the window mechanisim

count_down(5)
timer_text = canvas.create_text(100,130,text="00:00", fill="white",fonT=(FONT_NAME,35,"bold"))

start_button = Button(text="start",command=start_timer)
start_button.grid(column=0,row=2)
```

### 258 - Dynamic Typing
Dynamic typing is a feature in some programming languages where the type of a variable is determined at runtime, rather than being explicitly defined by the programmer at compile time. This means that a variable can be assigned different types of values throughout the program's execution without needing to declare its type.

For example, in a dynamically typed language like Python:
```
x = 10      # x is an integer
x = "hello" # now x is a string
```
Here, x can hold an integer and then be reassigned to hold a string without causing an error. The language interpreter keeps track of the data type of x as it changes.
Key points of dynamic typing:

1. No need for explicit type declarations.
2. The type is inferred based on the value assigned.
3. Flexibility to reassign variables to different types.
4. Potentially more error-prone, as type-related issues only show up at runtime.


```Python
if count_sec < 10:
    count_sec = f"0{count_sec}

```

### 260 - Congratulations
Check the final code for all the functionality
Congratulations you have completed Day 28
