"""
Import random library and content in other
Python files, for game operation.
"""

import random

from wordlist import words
from hangman_graphics import hangman_figures

print("""
 ▄▄   ▄▄ ▄▄▄▄▄▄ ▄▄    ▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄ ▄▄    ▄
█  █ █  █      █  █  █ █       █  █▄█  █      █  █  █ █
█  █▄█  █  ▄   █   █▄█ █   ▄▄▄▄█       █  ▄   █   █▄█ █
█       █ █▄█  █       █  █  ▄▄█       █ █▄█  █       █
█   ▄   █      █  ▄    █  █ █  █       █      █  ▄    █
█  █ █  █  ▄   █ █ █   █  █▄▄█ █ ██▄██ █  ▄   █ █ █   █
█▄▄█ █▄▄█▄█ █▄▄█▄█  █▄▄█▄▄▄▄▄▄▄█▄█   █▄█▄█ █▄▄█▄█  █▄▄█
      """)

print(
    "Welcome to my Hangman game! Guess letters to discover the random word.\n"
)

print("""Rules:

-Enter a letter when prompted in the terminal.
-Hint - you're guessing the name of a wild animal.
-If you make 6 wrong guesses, the game ends.
-Good luck!
    """)

username = None


def welcome_user():
    """
    Function to allow the player to input their name
    before the game begins. The name field only
    accepts letters.
    """
    global username
    while True:
        username = input('Please enter your name:\n')

        if not username.isalpha():
            print('Name must include only letters.')
            continue
        else:
            print(f'Welcome, {username}!')
            print('================================')

            break


def run_game():

    """
    Main function for game operation
    """
    random_word = random.choice(words)
    for x in random_word:
        print("_", end=" ")

    print("\nHint: The word has", len(random_word), "letters")

    letters_guessed = []
    wrong_guesses = 0
    wrong_letters_guessed = []
    failure_count = 6

    while wrong_guesses != 6:
        print("\nLetters guessed so far: ")
        for letter in letters_guessed:
            print(letter, end=" ")
        # variable for player guesses
        guess = input("\nEnter a letter: \n").lower()

        if guess.isalpha() is False:
            print("This game only accepts letters!")
            continue

        if len(guess) > 1:
            print("Please enter one letter at a time.")
            continue

        if guess in letters_guessed:
            print("Letter already guessed. Try a different letter.")
            continue

        if guess in random_word:
            print(
                f"Correct! There is one or more '{guess}' in the secret word."
            )

        else:
            failure_count -= 1
            wrong_guesses += 1
            wrong_letters_guessed.append(guess)
            print(
                f"Wrong guess! {failure_count} turn(s) left"
            )
            hangman_figures(len(wrong_letters_guessed))

        letters_guessed.append(guess)
        wrong_letter_count = 0

        for letter in random_word:
            if letter in letters_guessed:
                print(f"{letter}", end=" ")
            else:
                print("_", end=" ")
                wrong_letter_count += 1

        if wrong_letter_count == 0:
            print(f"\nCongrats! The secret word was {random_word}. You win!")
            break

    else:
        print("""\nBad luck, you lost. Better luck next time!""")
        print(f"The correct word was {random_word}")


def ask_to_play_again():
    """
    Function to ask the player if they want to restart
    the game.
    """
    answer = input("Do you want to play another game y/n?\n")
    if answer == "y":
        main()

    elif answer == "n":
        print("""
╔═══╗          ╔╗╔╗           
║╔═╗║          ║║║║           
║║ ╚╝╔══╗╔══╗╔═╝║║╚═╗╔╗ ╔╗╔══╗
║║╔═╗║╔╗║║╔╗║║╔╗║║╔╗║║║ ║║║╔╗║
║╚╩═║║╚╝║║╚╝║║╚╝║║╚╝║║╚═╝║║║═╣
╚═══╝╚══╝╚══╝╚══╝╚══╝╚═╗╔╝╚══╝
                     ╔═╝║     
                     ╚══╝   

""")


def main():
    """
    Main function to run the game.
    """
    if username is None:
        welcome_user()
    run_game()
    ask_to_play_again()


main()
