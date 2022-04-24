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
    "Welcome to my Hangman game! Guess letters to discover the random word\n"
)

print("""Rules:

-Enter a letter when prompted in the terminal.
-Hint - you're guessing the name of a wild animal.
-If you make 6 wrong guesses, the game ends.
-Good luck!
    """)

def welcome_user():
    """
    This function allows the player to input their name
    before the game begins. The name field only
    accepts letters.
    """
    username = None
    while True:
        username = input('Please enter your name:\n')

        if not username.isalpha():
            print('Name must include only letters.')
            continue
        else:
            print(f'Welcome, {username}!')
            print('================================')

            break

welcome_user()