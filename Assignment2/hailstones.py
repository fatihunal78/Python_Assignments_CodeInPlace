"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""

import math

def main():

    steps = 0
    user_input=int(input("Enter a number: "))
    calculation=user_input

    while calculation != 1:
        if calculation % 2 == 1:
            print(str(calculation) + " is odd, so I make 3n + 1: " + str(calculation * 3 + 1))
            calculation = calculation * 3 + 1
        else:
            print(str(calculation) + " is even, so I take half: " + str(calculation // 2))
            calculation = calculation // 2
        steps +=1

    print("The process took " + str(steps) + " to reach 1")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
