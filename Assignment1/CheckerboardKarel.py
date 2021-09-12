from karel.stanfordkarel import *


def main():
    # TODO write your solution here
    put_beeper()
    while front_is_clear():
        turn_left()
        move()
        turn_right()
        move_forward()
        put_beeper()


def move_forward():
    for i in range(2):
        move()


# There is no need to edit code beyond this point

def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()


if __name__ == "__main__":
    run_karel_program()
