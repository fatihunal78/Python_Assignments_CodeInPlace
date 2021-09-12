import time
import random

from colorama import init
from termcolor import colored
init(autoreset=True, convert=True)

PHASE_TIME_S = 10

def print_intro():
    """
    Function: print intro
    Prints a simple welcome message
    """
    print("This is the Stroop test! Name the font-color used:")
    print_in_color("red", "red")
    print_in_color("blue", "blue")
    print_in_color("pink", "pink")


def random_color_name():
    """
    Function: random color
    Returns a string (either red, blue or pink) with equal likelihood
    """
    return random.choice(["red", "blue", "pink"])


def print_in_color(text, font_color):
    """
    Function: print in color
    Just like "print" but this time, you can specify the font-color
    """
    if font_color == "pink": # magenta is a lot to type...
        font_color = "magenta"
    print(colored(text, font_color, attrs=["bold"]))

def main():
    print_intro()
    n_correct_control = run_tests(True)
    n_correct_flipped = run_tests(False)
    print('\nDone!')
    print('control', n_correct_control)
    print('flipped', n_correct_flipped)

def run_tests(is_control):
    start_time = time.time()
    n_correct = 0
    while time.time() - start_time < PHASE_TIME_S:
        correct = run_single_test(is_control)
        if correct:
            n_correct += 1
    return n_correct

def run_single_test(is_control):
    print('')
    color_name = random_color_name()
    font_color = get_font_color(color_name, is_control)
    print_in_color(color_name, font_color)
    response = input('What color ink is the word written in? ')
    if response != font_color:
        print('Correct answer was: ' + font_color)
    return response == font_color

def get_font_color(color_name, is_control):
    if is_control:
        return color_name
    while True:
        next_choice = random_color_name()
        if next_choice != color_name:
            return next_choice



if __name__ == "__main__":
    main()