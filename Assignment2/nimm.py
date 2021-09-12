"""
File: nimm.py
-------------------------
Add your comments here.
"""

import math

def main():
    total_num_stones = 20
    player = 1

    while total_num_stones > 0:
        print("There are " + str(total_num_stones) + " stones left")
        removed_stones= int(input("Player " + str(player) + " would you like to remove 1 or 2 stones?" + " "))
        if (removed_stones == 1) or (removed_stones == 2):
            total_num_stones = total_num_stones - removed_stones
        else:
            removed_stones = int(input("Please enter 1 or 2:" + " "))
            total_num_stones = total_num_stones - removed_stones

        print("")
        if player == 1:
            player = 2
        else:
            player = 1

    print("Player " + str(player) + " wins!")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
