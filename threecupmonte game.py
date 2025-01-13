#!/usr/bin/env python
# coding: utf-8

from random import shuffle

# Function to shuffle the list
def shuffle_list(mylist):
    shuffle(mylist)  # Shuffles the list in place
    return mylist  # You can return mylist for clarity, but shuffle modifies it in place

# Function to get player's guess
def player_guess():
    guess = ""
    while guess not in ['0', '1', '2']:
        guess = input('PICK A NUMBER: 0, 1, OR 2: ')
    return int(guess)

# Function to check the guess
def check_list(game_list, guess):
    if game_list[guess] == 'O':
        print("Correct! 👏")
    else:
        print("Wrong guess! 😢")
    print(game_list)

# Main game logic
if __name__ == "__main__":
    # Initial list
    game_list = [' ', 'O', ' ']
    
    # Shuffle list
    mixedup_list = shuffle_list(game_list)
    
    # Get user's guess
    guess = player_guess()
    
    # Check the guess
    check_list(mixedup_list, guess)
