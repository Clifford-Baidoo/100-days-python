## Day 12 - Scope and number Guessing Game

### 115 -Namespaces Local vs Global
Scope - a scope refers to the region of the program where a particular variable or name is accessible.

```python
######### Scope #########
enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength) #For this print statement you eill get an error because potion_strength = 2 is a local scope inside the function

#Global Scope
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()
#if we were to call player_health anywhere it would work because it is a global variable or scope
```
In this code the print statement outside will print enemies as 1 and the one inside the function as 2
And this is because of scope

Local scopes exist inside the function global exist everywhere so it is not based in one function

Namespace - Namespace is anything that you give a name and it is valid in certain scopes

### 116 - Does Python have Block Scope
Block scope refers to the concept where variables declared inside certain blocks of code (such as loops or conditionals) are only accessible within that block.

```Python
if True:
    x = 10  # This variable is accessible outside the block

print(x)  # Outputs: 10

```
In the example above, x is accessible outside the if block because Python does not restrict the scope of variables declared inside the if block.

### 117 - How to Modify a Global Variable

```Python
#Modyifying Global Scope
enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside functionn: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
```

If we want to use a global scope inside a function we must let it know that it is a global scope or it will work and the best way to do that is to add global to the function name

But it is confusing to modify a global scope that way because you can get erros so the best thing to do is return it

```Python
#Modyifying Global Scope
enemies = 1

def increase_enemies():
    global enemies #Instead of doing this
    enemies = 2
    print(f"enemies inside functionn: {enemies}")
    return enemies + 1 #You can just return the Output

increase_enemies()
print(f"enemies outside function: {enemies}")
```
### 118 - Python Constants and Global Scope
Global Constants is something you define and you never want to change again
like:
```
pi = 3.14159
#but if you want to make it like that you have to change the name to upper #case to make you and people know that it is a global Constants
PI = 3.14159
```

### 119 - Final Project
The Number Guessing Game
You have to do this yourself

Output
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100
Choose a difficulty.Type 'easy' or 'hard'

On easy the user has 10 attempts and everytime the user enters a number tell the user whether the number is correct , too high or too low

Do same for hard level but the user gets 5 attempts

### 120 - Solution
Check the last code for solution

### 121 - Congratulations
Congratulations you have completed day 12
