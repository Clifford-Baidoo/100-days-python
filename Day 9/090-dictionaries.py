programming_dictory = {
 "Bug":"An error in a program that prevents the program from running as expected",
 "Function":"A piece of code that you can easily call over and over again",
 "Loop":"The action of doing something over and over again"
 }

print(programming_dictory["Bug"])

programming_dictory["Loop"] = "The action of doing something over and over again."
print(programming_dictory)

empty_dictionary = {}

programming_dictory = {}
print(programming_dictory)

programming_dictory["Bug"] = "A moth in my computer"
print(programming_dictory)

for key in programming_dictory:
    print(key)
    print(programming_dictory[key])