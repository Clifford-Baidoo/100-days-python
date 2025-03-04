## Day 30 - Erros,Exceptions and Saving JSON Data

### 268 - Day 30 goals
We are going to learn about errors and exceptions and JSON
we will also improve our password manager with a search function

### 269 - Catching Exceptions

There are some types of errors we face
FileNotFound
TypeError and stuff

Excpetions are basically the errors we face in our program
and catching exceptions is just catching the errors so they don't fail badly

try: Something that might cause an excpetion
Except: Do this if there was an exception
else: Do this if ther were no exceptions
finally: Do this no matter what happens

```Python
try:
    file = open("a_file.txt")
except:
    file = open("a_file.txt")

```

