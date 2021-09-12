"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""
import math

def main():

    print("This program subtracts one number from another.")
    number_1 = float(input ("Enter first number: "))
    number_2 = float(input ("Enter second number: "))
    result = number_1 - number_2
    print ("The result is " + str(result))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
