def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn():
    turn_right()
    move()
    turn_right()
    move()

while not at_goal():
    if not wall_on_right():
        turn()
    elif wall_in_front():
        turn_left()
    elif front_is_clear():
        move()
