from karel.stanfordkarel import *

def main():
    # TODO write your solution here
    put_beeper()
    while front_is_clear():
        ramp_climb()

# There is no need to edit code beyond this point

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

def ramp_climb():
    turn_left()
    if front_is_clear():
        move()
        turn_right()
        move()
        move()
        put_beeper()


if __name__ == "__main__":
    run_karel_program()