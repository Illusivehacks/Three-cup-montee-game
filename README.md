# Shuffle and Guess Game 🎲

A fun and interactive Python command-line game where you try to find the hidden "O" in a shuffled list. Perfect for beginners learning Python basics like list manipulation, user input, and randomness.

---

## Features
- **Interactive Gameplay**: Players guess the position of the "O".
- **Randomized Outcomes**: The list is shuffled each time, keeping the game exciting.
- **Beginner-Friendly**: A simple and educational project for learning Python.

---

## How to Play
1. Run the script using Python 3:
   ```bash
   python threecupmonte game.py
   
2. The program shuffles a list: [' ', 'O', ' '].
3. You will be prompted to guess the position of the "O" by entering 0, 1, or 2.
4. The program evaluates your guess and provides feedback:
      Correct Guess: Prints "Correct! 👏"
      Incorrect Guess: Prints "Wrong guess! 😢"
5. The shuffled list is revealed to show the correct position.


Code Overview
1. shuffle_list(mylist): Shuffles a given list randomly.
2. player_guess(): Ensures user input is valid and returns the guessed position.
3. check_list(game_list, guess): Compares the user's guess with the shuffled list and displays results.
4. Main Game: Combines all the functions to run the game interactively.

Customization
Change the symbols in the list to suit your preference (e.g., replace 'O' with 'X').
Add a scoring system or implement multiple rounds.
Expand the game with more advanced Python concepts like GUIs using Tkinter.


Requirements
Python 3.6 or later installed on your system.


License
This project is licensed under the MIT License. Feel free to use, modify, and share it.

Enjoy playing and learning! 🚀
