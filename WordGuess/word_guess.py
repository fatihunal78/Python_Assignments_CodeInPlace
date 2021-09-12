"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    """
    Add your code (remember to delete the "pass" below)
    """
    tempword=""
    tempword_length=0
    guess_count=INITIAL_GUESSES

    # creating ---- for the random secret word
    print("The word now looks like this: ", end='')
    for i in range(len(str(secret_word))):
        tempword +="-"
    print(tempword)
    print("You have " + str(guess_count) + " guesses left")

    # calculating the length of secret word
    tempword_length=len(tempword)

    while(guess_count > 0):

        user_input= input("Type a single letter here, then press enter: ")

        # if the user estimates the secret word at one estimate the program returns congratulations.
        if user_input == secret_word:
            print("Congratulations, the word is:", secret_word, end='')
            break

        # checking user input whether it is only one character.
        if user_input.isalpha():
            if (len(user_input) == 1):
                user_input = user_input.upper()

                #user inputs the same estimate again, nothing changes.
                if (user_input in tempword):
                    print("The word now looks like this: ", tempword)
                    print("You have " + str(guess_count) + " guesses left")
                    continue

                # updating the ----- version of secret word according to estimates
                if secret_word.find(user_input) >= 0:
                    for i in range(tempword_length):
                        templist = list(tempword)
                        if(secret_word[i]==user_input):
                            templist[i] = user_input
                        tempword = "".join(templist)
                else:
                    print("There are no " + user_input + "'s in the word")

                guess_count-=1
            else:
                print("Guess should only be a single character.")
        else: # if the estimate is not an alphabetic character.
            print("That guess is incorrect.")
            guess_count -= 1

        # if the secret word is estimated correctly before the rights of estimates finish, the program returns success.
        if "-" not in tempword:
            print("Congratulations, the word is:", secret_word, end='')
            break
        # if the secret word can not be estimated correctly before the rights of estimates finish, the program returns failure.
        elif "-" in tempword and guess_count == 0:
            print("Sorry, you lost. The secret word was:", secret_word, end='')
            break

        print("The word now looks like this: ", tempword)
        print("You have " + str(guess_count) + " guesses left")

def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    dictionary = []

    # reading text file
    with open(LEXICON_FILE) as word:
        for line in word:
            dictionary.append(line.strip())

    # returning random item from dictionary
    return dictionary[random.randrange(len(dictionary))]


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()