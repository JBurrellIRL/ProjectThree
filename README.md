# JB's Hangman Game

Site URL: https://jbs-hangman-game.herokuapp.com/

JB's Hangman game is a terminal-based game, where the player's objective is to identify a hidden word, chosen randomly by the game, of which only the number of letters in the word is initially revealed. The player guesses letters in the alphabet - usually starting with vowels, as these are the most commonly-used letters. If their guess is present in the hidden word, each instance of their guessed letter is revealed by the game. If their guess is incorrect, a portion of the hangman's body is drawn on a gallows. 

The game ends with either the player correctly guessing the randomly-chosen word, or with the hangman's body being completed if the player fails to guess the hidden word. To help the player, the player receives a hint at the start of the game, after they enter their name, and also a record is kept of previously-guessed letters, so that the player can keep track of their guesses.

## How To Play

* The player first needs to enter their name. Once they do this, the game then begins. 
* The helpful hint described above will appear, and the player then plays the game by guessing random letters. 
* When they guess a letter correctly, the underscore in the random word will be replaced by the correctly guessed letter.
* The player can only make 6 incorrect guesses before the game is ended. 
* Once the player either succeeds or fails, the player is then offered the opportunity to restart the game again. If they decide not to restart the game, the game terminates.

## UX

* This game is a terminal-based game, that runs immediately when first launched. The game can also be run by clicking on the "Run Program" button built into the Heroku UI. Upon first launching the game, the player is presented with a welcome message, a bullet-point list of the rules of the game, and an invitation to enter their name, as shown in this screenshot:

![Game Launch](https://github.com/JBurrellIRL/ProjectThree/blob/main/assets/gamelaunch.png?raw=true)

* Once the player enters their name, the game then begins. The "name" input allows only letters, and returns an error if numbers, symbols or blank spaces are entered.

* Once the player has successfully entered their name, the game is running. The player is prompted to enter a letter as their guess - above the input field, they're also shown a welcome message along with the text-written "Hint" and an area with underscores representing each unguessed letter in the hidden word, to help them with the game. Under this is an area that displays letters the player has already guessed.

* If the player makes a correct guess, they receive a message saying that they guessed a letter correctly, and that one or more instance of the guessed letter is found in the game. Below this, the correctly guessed letter will replace the underscore in each instance of it appearing in the hidden word. Also, the "Letters already guessed" area is updated with the letter guessed.

* If the player makes a wrong guess, they receive a message saying that they were incorrect. Below this, they receive a text warning that their guess was wrong, and a portion of a hangman graphic also appears. This graphic then progresses with more and more of the stick figure added with each wrong guess.

* If the player wins the game, they receive a message in the terminal to congratulate them on winning the game, and confirms what the hidden word was. If the player loses, the Hangman graphic is completed and they recieve a text message in the terminal saying that they lost the game. The game also tells them what the hidden word was.

* The player is then given the option to play the game again if they wish to. The entries 'y' or 'n' will then take the appropriate action, based on the player entry. If the player elects to play for a second time, they don't have to re-enter their name again, and the game generates a new hidden word to begin the game again. The game can continue to be played on repeat until the player enters 'n' in response to being asked if they want to play again, at which point the game terminates.

### Features Left to Implement

In the future, I'd like to expand this game to pick random words from different areas (outside of just wild animals) and then to show a hint to the player that's appropriate to the hidden word. It would also be nice to create a "leaderboard" system, that tracks players guessing the hidden word in the least amount of tries.

## Technologies Used

Below is a list of languages, plugins and other tools used to create and develop this website. 

* [Python3](https://www.python.org/).
* Git - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* GitHub - GitHub is used to store the projects code after being pushed from Git.
* Heroku.

## Testing

* During the development of this game, I constantly tested it in the GitPod terminal to ensure that its functionality was expected and working as intended. I validated my code through the PEP8 Python validator before committing it and then pushing it to GitHub.

* Once the app was deployed to Heroku, I tested it through the deployed Heroku link, to make sure it worked as I intended it to.
* I validated my code through the PEP8 Python validator, where it returns no errors. Screenshot here:

![Pep8](https://github.com/JBurrellIRL/ProjectThree/blob/main/assets/pep8.png?raw=true)

### Manual Testing

* Upon launching the game, the player is prompted to enter their name. I verified that only letters (uppercase and/or lowercase letters) are accepted in this field. If the player tries to enter other characters, or a space, an error is returned to state "Name must include only letters".

* When actually playing the game and guessing letters, the player is only permitted to enter letters (either uppercase or lowercase). Uppercase letters are converted to lowercase. If the player tries to enter other characters such as letters or symbols, or a space, an error states "This game only accepts letters!". 

* If the player tries to enter more than one letter at a time, the game returns an error stating "Please enter one letter at a time".

* If the player guesses a letter that they've already guessed, the game returns an error saying "Letter already guessed. Try a different letter". The letter is then not added to the "Letters already guessed" line a second time, as the letter already exists there.

* Once the player reaches the end of the game, they receive an option to play again whether they were successful or unsuccessful. I verified that entering 'y' (in upper or lower case) starts the game again, without asking them for their name a second time. Entering 'n' (in upper or lower case) terminates the game with a "Goodbye" message. Entering any other character returns an error that states: "Please enter either y or n."


### Bugs

* I encountered issues with the game accepting invalid characters when developing the game - such as it not recognising capital letters as being the same as lowercase for the purpose of this game, blank space entries and numeric entries. These were resolved through using if statements in the main game while loop.
* Resolved an issue where entering a character other than 'y' or 'n' at the end of the game terminated the game entirely.
* No further unresolved bugs have been detected.

### Accessibility

* The game is purely Python-based and does not include any images or CSS.

## Deployment

This project was deployed using Code Institute's Heroku terminal. The game was created using Code Institute's GitPod template for Milestone Project 3, and deployed to GitHub. I also created an account on Heroku, and connected my GitHub repo to Heroku through the terminal method. 

### Manual Deployment

Steps for deployment:
* Fork or clone this repository.
* Create a new Heroku App.
* Add a config var of PORT: 8000.
* Set the app buildpacks to Python and NodeJS (in this order).
* Link the Heroku App to the repository.

For local deployment:

* Clone this project from GitHub.
* Ensure that Python is installed on your system.
* Run the run.py file to run the game.

## Credits

Resources used include the following:

* Code Institute - course content, Love Sandwiches project and also the "Portfolio 3 Project Scope" video created by Matt Rudge.
* Udemy Python course, which I am also taking in parallel to this Code Institute course. I used this for help with Python functions and syntax. 
* A big thanks to my mentor, Jack, for his advice during our mentoring sessions.