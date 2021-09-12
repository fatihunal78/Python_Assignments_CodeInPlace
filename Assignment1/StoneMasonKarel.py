from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    # putting markers starting from the first position and leaves 3 points blank and puts a marker (beeper)
    # to the 5th following position. It checks the width of dimension at every move
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        for i in range(4):
            if front_is_clear():
                move()
        if no_beepers_present():
            put_beeper()

    # after putting markers karel turns back to the initial position.
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()
    turn_left()

    # karel starts to move again and when it sees a marker it turns upward and completes the missing beepers.
    while front_is_clear():
        if beepers_present():
            turn_left()
            while front_is_clear():
                if no_beepers_present():
                    put_beeper()
                    move()
                else:
                    move()
            if no_beepers_present():
                put_beeper()

            turn_left()
            turn_left()
            while front_is_clear():
                move()
            turn_left()
            move()
        else:
            move()

    # this code block is for the beeper check (if missing placing) of the last row
    if beepers_present():
        turn_left()
        while front_is_clear():
            if no_beepers_present():
                put_beeper()
                move()
            else:
                move()
        if no_beepers_present():
            put_beeper()

        # after completing the mission karel turns back to the lower-rightmost point of the rectangular shape.
        turn_left()
        turn_left()
        while front_is_clear():
            move()
        turn_left()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program()
