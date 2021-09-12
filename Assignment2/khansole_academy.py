"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random
import math

MIN_NUM = 10
MAX_NUM = 99

def main():

    count = 0
    while count < 3:
        number_1 = random.randint(MIN_NUM, MAX_NUM)
        number_2 = random.randint(MIN_NUM, MAX_NUM)
        total = number_1 + number_2
        print("What is " + str(number_1) + " + " + str(number_2) + "?")
        answer = int(input("Your answer: "))

        if total != answer:
            count = 0
            print("Incorrect. The expected answer is " + str(total))
        else:
            count += 1
            print("Correct! You've gotten " + str(count) + " correct in a row.")

    print("Congratulations! You mastered addition.")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
