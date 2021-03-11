#Reeborg's World Hurdles 4 

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while front_is_clear():
        move()
    if wall_in_front():
        turn_left()
        
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
    
    
    
