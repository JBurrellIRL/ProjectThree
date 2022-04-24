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
    "Welcome to my Hangman game! Guess the letters to uncover the random word.\n"
)

print("""Rules:

-Enter a letter when prompted in the terminal.
-Hint - you're guessing the name of a wild animal.
-If you make 6 wrong guesses, the game ends.
-Good luck!
    """)