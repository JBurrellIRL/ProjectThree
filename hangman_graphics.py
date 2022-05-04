def hangman_figures(x):
    """
    Function to print the hangman graphic, that progresses through
    different graphics, as player gets guesses wrong. Code obtained
    from YouTube video.
    """
    if x == 1:
        print("\n+====+ ")
        print("|      | ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("===+")
    elif x == 2:
        print("\n+====+ ")
        print("|      | ")
        print("|      O ")
        print("|        ")
        print("|        ")
        print("===+")
    elif x == 3:
        print("\n+====+ ")
        print("|      | ")
        print("|      O ")
        print("|      | ")
        print("|        ")
        print("===+")
    elif x == 4:
        print("\n+====+ ")
        print("|      | ")
        print("|      O ")
        print("|     /| ")
        print("|        ")
        print("===+")
    elif x == 5:
        print("\n+====+ ")
        print("|      | ")
        print("|      O ")
        print("|     /|\ ")
        print("|        ")
        print("===+")
    elif x == 6:
        print("\n+====+ ")
        print("|      | ")
        print("|      O ")
        print("|     /|\ ")
        print("|     / \ ")
        print("===+")
