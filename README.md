# JB's Hangman Game

Site URL: https://jbs-hangman-game.herokuapp.com/

JB's Hangman game is a terminal-based game, where the goal is to guess the random word by guessing different letters until the word is complete. The player is presented with an invitation to enter their name when the game initially starts, and then is given a hint to let them know how many letters the random word contains - both with a message in text, and also a series of underscores to represent the missing letters in the random word.

## How To Play

* The player first needs to enter their name. Once they do this, the game then begins. 
* The helpful hint described above will appear, and the player then plays the game by guessing random letters. 
* When they guess a letter correctly, the underscore in the random word will be replaced by the correctly guessed letter.
* The player can only make 6 incorrect guesses before the game ends. 
* Once the player either succeeds or fails, the player is then offered the opportunity to restart the game again. If they decide not to restart the game, the game ends.

## UX

* This game is a terminal-based game, that runs immediately when first launched. The game can also be run by clicking on the "Run Program" button built into the Heroku UI. Upon first launching the game, the user is presented with a welcome message, a bullet-point list of the rules of the game, and an invitation to enter their name, as shown in this screenshot:

![Game Launch](screenshot)

* Once the player enters their name, the game then begins. The "name" input allows only letters, and returns an error if numbers, symbols or blank spaces are entered, as shown here:

![Enter Name](screenshot)

* Once the player has successfully entered their name, the game is running. The player is prompted to enter a letter as their guess - above the input field, they're also shown a welcome message along with the text-written "Hint" and an area with underscores representing each unguessed letter. Under this is an area that displays letters the player has already guessed. Screenshot here:

![Game has begun](screenshot)

* If the player guesses a letter correctly, they receive a message saying that they were correct, and that one or more of the guessed letter is found in the game. Below this, the correctly guessed letter will replace the underscore in each instance of it appearing in the random word. Also, the "Letters already guessed" area is updated with the letter guessed. Screenshot here:

![Correct letter guess](screenshot)

* If the player guesses a letter wrongly, they receive a message saying that they were incorrect, and that the letter does not appear in the random word. Below this, they receive a text warning that their guess was wrong, and a hangman graphic also appears. This graphic then progresses with more and more of the stick figure added with each guess. Screenshot here:

![Incorrect letter guess](screenshot)

* If the player wins the game, they receive a message in the terminal that states they've won the game, and confirms what the correct word was. Here's a screenshot of that:

![Player Wins](screenshot)

* If the player loses, the Hangman graphic is completed and they recieve a text message in the terminal saying that they lost the game. Screenshot:

![Player Lost](screenshot)

* As noted above, the player is given the option to play the game again if they desire. The entries 'y' or 'n' will then take the appropriate action, based on the player entry. Entering any  If the player elects to play for a second time, they don't have to re-enter their name again, as shown here:

![play-game-2](screenshot)

* While the game is in operation, only letters are accepted as valid entries in the terminal. The game returns an error if blank space, symbol, number or double-letter entries are submitted. Capital letters are converted to lower-case letters to ensure that the game functions. Here's a screenshot to show that:

![Errors](screenshot)

### Features Left to Implement

In the future, I'd like to expand this game to pick random words from different areas (outside of just wild animals) and then to show a hint to the player that's appropriate to the random word.

## Technologies Used

Below is a list of languages, plugins and other tools used to create and develop this website. 

* [Python3](https://www.python.org/).
* Git - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* GitHub - GitHub is used to store the projects code after being pushed from Git.

## Testing

* During the development of this game, I constantly tested it in the terminal to ensure that its functionality was expected and working as intended. I validated my code through the PEP8 Python validator before committing it and then pushing it to GitHub.

* Once the app was deployed to Heroku, I tested it through the deployed Heroku link, to make sure it worked as I intended it to.
* I validated my code through the PEP8 Python validator, where it returns no errors. Screenshot here:

![Pep8](screenshot)


### Bugs

* I encountered issues with the game accepting invalid characters when developing the game - such as it not recognising capital letters as being the same as lowercase for the purpose of this game, blank space entries and numeric entries. These were resolved through using if statements in the main game while loop.
* Resolved an issue where entering a character other than 'y' or 'n' at the end of the game terminated the game.
* No further unresolved bugs have been detected.

### Accessibility

* The game is purely Python-based and does not include any images or CSS.

## Deployment

This project was deployed using Code Insitute's Heroku terminal. The game was created using Code Institute's GitPod template for Milestone Project 3, and deployed to GitHub. I also created an account on Heroku, and connected my GitHub repo to Heroku through the terminal method. 

## Credits

Resources used include the following:

* Code Institute - course content, Love Sandwiches project and also the "Portfolio 3 Project Scope" video created by Matt Rudge.
* Udemy Web Developer Bootcamp course, which I am also taking in parallel to this Code Institute course. I used this for help with Python functions and syntax. 
* A big thanks to my mentor, Jack, for his advice during our mentoring sessions.