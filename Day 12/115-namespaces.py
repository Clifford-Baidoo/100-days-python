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

'''drink_potion()
print(potion_strength) #For this print statement you eill get an error because potion_strength = 2 is a local scope inside the function'''

#Global Scope
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()
#if we were to call player_health anywhere it would work because it is a global variable or scope