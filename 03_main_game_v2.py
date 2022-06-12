# Python Program to illustrate
# Hangman Game
import random
from random import randint
from collections import Counter

# images = ['''
#             ___________.._______
#           | .__________))______|
#           | | / /      ||
#           | |/ /       ||
#           | | /        ||
#           | |/         ||
#           | |          ||ˍ
#           | |          (\\__৲
#           | |           `--ˊ
#           | |
#           | |
#           | |
#           | |
#           | |
#           | |
#           | |
#           | |
#           | |
#           ''', '''
#             ___________.._______
#           | .__________))______|
#           | | / /      ||
#           | |/ /       ||
#           | | /        ||
#           | |/         ||
#           | |          ||.-''.
#           | |          |/  _  \\
#           | |          ||  ☉/☉|
#           | |          (\\◝_ .'
#           | |           `--'
#           | |
#           | |
#           | |
#           | |
#           | |
#           | |
#           | |
#           | |
#           | |
# ''', '''
#     ___________.._______
#           | .__________))______|
#           | | / /      ||
#           | |/ /       ||
#           | | /        ||
#           | |/         ||
#           | |          ||.-''.
#           | |          |/  _  \\
#           | |          ||  ☉/☉|
#           | |          (\\◝_ .'
#           | |           `--'
#           | |         .-`--'.
#           | |         Y . . Y
#           | |          |   |
#           | |          | . |
#           | |          |   |
#           | |
#           | |
#           | |
#           | |
#           | |
# ''', '''
#   ___________.._______
#           | .__________))______|
#           | | / /      ||
#           | |/ /       ||
#           | | /        ||
#           | |/         ||
#           | |          ||.-''.
#           | |          |/  _  \\
#           | |          ||  ☉/☉|
#           | |          (\\◝_ .'
#           | |           `--'
#           | |         .-`--'.
#           | |        /Y . . Y
#           | |       // |   |
#           | |      //  | . |
#           | |     ')   |   |
#           | |
#           | |
#           | |
#           | |
#           | |
# ''', '''
#             ___________.._______
#           | .__________))______|
#           | | / /      ||
#           | |/ /       ||
#           | | /        ||
#           | |/         ||
#           | |          ||.-''.
#           | |          |/  _  \\
#           | |          ||  ☉/☉|
#           | |          (\\◝_ .'
#           | |           `--'
#           | |         .-`--'.
#           | |        /Y . . Y\
#           | |       // |   | \\
#           | |      //  | . |  \\
#           | |     ')   |   |   (`
#           | |
#           | |
#           | |
#           | |
# ''', '''
#   ___________.._______
#           | .__________))______|
#           | | / /      ||
#           | |/ /       ||
#           | | /        ||
#           | |/         ||
#           | |          ||.-''.
#           | |          |/  _  \\
#           | |          ||  ☉/☉|
#           | |          (\\◝_ .'
#           | |           `--'
#           | |         .-`--'.
#           | |        /Y . . Y\
#           | |       // |   | \\
#           | |      //  | . |  \\
#           | |     ')   |   |   (`
#           | |          ||-
#           | |          ||
#           | |          ||
#           | |          ||
#           | |         / |
# ''', '''
#
#   ___________.._______
#           | .__________))______|
#           | | / /      ||
#           | |/ /       ||
#           | | /        ||
#           | |/         ||
#           | |          ||.-''.
#           | |          |/  _  \\
#           | |          ||  ☉/☉|
#           | |          (\\◝_ .'
#           | |           `--'
#           | |         .-`--'.
#           | |        /Y . . Y\
#           | |       // |   | \\
#           | |      //  | . |  \\
#           | |     ')   |   |   (`
#           | |          ||-||
#           | |          || ||
#           | |          || ||
#           | |          || ||
#           | |         / | | \
# ''']
word_list = ["one", "two", "three", "four", "five", "six"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
attempt = 0
unused_letter = []
display = []
for _ in range(word_length):
    display += "_"

end_of_game = False

while attempt != 7:
    guess = input("Guess a letter: ").lower()
    # Check guessed letter
    while not guess.isalpha():
        print("Please enter a letter.")
        guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed {guess}!")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(display)
        if letter != guess:
            unused_letter.append(letter)
            print(f"Not used letter: {unused_letter}")

    if guess not in chosen_word:
         unused_letter.append(guess)
            print(f"Not used letter: {unused_letter}")
        attempt += 1
        print(display)
        

    if "_" not in display:
        end_of_game = True
        print("You win!")
    # print(images[attempt])

print(f"You lose!, the word is {chosen_word}")
