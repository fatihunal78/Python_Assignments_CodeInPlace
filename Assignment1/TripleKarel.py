from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():

    # the code runs for each rectangular shape, then it runs for three times.
    for i in range(0, 19, 2):
        for i in range(3):
        paint_three_edges()
        turn_back()

    # karel turns itself to the desired position in the end
    turn_left()


# paints the three edges of each rectangular shape
def paint_three_edges():
    for i in range(3):
        while left_is_blocked():
            put_beeper()
            move()
        turn_left()
        move()


# turns back from the wrong position that karel reaches at the end of each third edge.
def turn_back():
    turn_left()
    turn_left()
    move()

# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program()
