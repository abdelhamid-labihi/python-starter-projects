# Python Guessing Game

This is a simple command-line Guessing Game application written in Python. It's a great project for beginners to get started with Python programming.

## Features

The application has the following features:

- Ask for the player's name
- Allow the player to choose the range of numbers for the guessing game
- Allow the player to guess a number within the chosen range
- Give hints if the guess is too high or too low
- Keep track of the number of attempts
- Display the current high score (minimum attempts)
- Allow the player to play again

## Code Explanation

The code is organized into a main loop and a function:

- `show_score()`: This function checks if there are any scores in `attempts_list`. If there are, it prints the current high score (minimum attempts). If not, it prints a message encouraging the player to start playing.

The main loop does the following:

- Welcomes the player and asks for their name
- Asks the player to choose the lower and upper bounds of the range of numbers for the guessing game
- Asks the player to guess a number within the chosen range
- Checks if the player's guess is too high, too low, or correct, and gives appropriate feedback
- Keeps track of the number of attempts
- Adds the number of attempts to `attempts_list` and displays the current high score
- Asks the player if they want to play again

## Strategy for Guessing

A good strategy for guessing the number in the least number of attempts is to use binary search. This involves guessing the middle number in the range, and then based on whether this guess is too high or too low, guessing the middle number in the remaining upper or lower half of the range, and so on.

For example, if the range is 1 to 100, you would first guess 50. If the feedback is "Too high", you would then guess the middle number in the range 1 to 49, which is 25, and so on.

## Running the Code Locally

To run this code on your local machine, follow these steps:

1. Make sure you have Python installed. You can download Python from [here](https://www.python.org/downloads/).

2. Save the code in a file named `guessing_game.py`.

3. Open a terminal/command prompt.

4. Navigate to the directory where you saved `guessing_game.py`.

5. Run the command `python guessing_game.py`.

You should now see the prompt "Hello player! Welcome to the guessing game!" and you can start playing!
