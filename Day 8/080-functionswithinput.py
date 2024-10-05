#Review:
#Create a function called greet()
#Write 3 print statements inside the function.
#Call the greet function and run your code

def greet():
    print("Hello,Good day")
    print("How do you do?")
    print("Isn't the weather nice today")

greet()

#Functions that allow for input
def greet_with_name(name):
    print(f"Hello {name},good day")
    print(f"How do you do {name}")

greet_with_name("Clifford")