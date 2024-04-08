## Rock Paper Scissors Game

This is a simple implementation of the game Rock, Paper, Scissors in Python. The game is played in the console.

### How to Run

To run the game, simply execute the `rock_paper_scissors.py` file in your Python environment.

### Code Explanation

The game uses a list and a dictionary to manage the game rules and choices.

```python
options = ["rock", "paper", "scissors"]
```

The `options` list contains the three possible choices in the game: rock, paper, and scissors.

```python
rules = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}
```

The `rules` dictionary defines the winning conditions. The keys are the player's choices and the values are what they beat. For example, `"rock" beats "scissors"`.

The game loop asks for the player's choice, generates a random choice for the computer, and then compares the two to determine the result.

```python
if player_choice == computer_choice:
    print("It's a tie!")
elif rules.get(player_choice) == computer_choice:
    print("You win!")
```

In the above code, `player_choice` is compared with `computer_choice`. If they are the same, it's a tie. If not, the game uses the `rules` dictionary to check if the player's choice beats the computer's choice. The `get` method is used to retrieve the value associated with the key in the dictionary. If the value associated with the player's choice (key) is the same as the computer's choice, the player wins.

### For Python Beginners

A dictionary in Python is a collection of key-value pairs. Each key is unique and the values can be anything. In this game, the keys are the player's choices (rock, paper, or scissors) and the values are what they beat. The `get` method is a way to retrieve the value for a given key from the dictionary. In this case, it's used to check if the player's choice beats the computer's choice according to the game rules.
