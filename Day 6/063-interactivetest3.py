'''def turn_right():
    for i in range(0,3):
        turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
 

def final():
    if front_is_clear():
        move()
    elif wall_in_front:
        jump()
        
while not at_goal():
    final()'''