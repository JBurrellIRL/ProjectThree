def get_hangman(x):
    """
    Function to print the hangman graphic, that progresses through
    different graphics, as player gets guesses wrong. 
    Code obtained from YouTube video.
    """
    if x == 1:
        print("\n+====+ ")
        print("|      | ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("===+")
    if x == 2:
        print("\n+====+ ")
        print("|      | ")
        print("|      O ")
        print("|        ")
        print("|        ")
        print("===+")
    if x == 3:
        print("\n+====+ ")
        print("|      | ")
        print("|      O ")
        print("|      | ")
        print("|        ")
        print("===+")
    if x == 4:
        print("\n+====+ ")
        print("|      | ")
        print("|      O ")
        print("|     /| ")
        print("|        ")
        print("===+")
    if x == 5:
        print("\n+====+ ")
        print("|      | ")
        print("|      O ")
        print("|     /|\ ")
        print("|        ")
        print("===+")
    if x == 6:
        print("\n+====+ ")
        print("|      | ")
        print("|      O ")
        print("|     /|\ ")
        print("|     / \ ")
        print("===+")