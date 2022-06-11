# Word checking function
def word_to_guess():
    global word, wordlist
    # Enter a word
    valid = False
    while not valid:
        error = "Please enter A WORD!"
        try:
            word = input("Enter a word that you want player to guess.\n"
                         ">>> ").upper()
            # Make sure it contains only alphabet characters.
            if word.isalpha():
                valid = True
            elif word == "":
                print(error)
            else:
                print(error)
        except ValueError:
            print(error)

    # Split the word into letters and put in a list
    wordlist = list(word)
    print(wordlist)
    wordlist = [i for i in word]
    print("\n" * 1000)
    return difficulty()

def difficulty():
    import time

    # Set up difficulty
    EASY = 10
    HARD = 5
    IMPOSSIBLE = 1

    # Introduction and instructions
    print("**** Welcome to 'What's the word?' Game ****")
    time.sleep(1)
    print("The rules are quite similar to 'Hangman':")
    print("- You have been given a word.")
    print("- You need to guess its letters.")
    print("- You can only enter 1 letter each guess.")
    print("- When you get all the letters, "
          "you need to guess what the word is.")
    print("- Unlike 'Hangman', when you get a correct letter, "
          "it won't get in its order in the word!")
    print()
    time.sleep(2)

    input("Press 'Enter' to start: ")
    print()

    # Let the players choose one difficulty mode
    global mistakes, difficult_mode
    valid = False

    while not valid:
        error = "Please choose 1 in 3 difficulties!"

        try:
            print("1 - Easy: You are allowed to have {} wrong.\n"
                  "2 - Hard: You are allowed to have {} wrong.\n"
                  "3 - Impossible: You are only allowed to have {} wrong.".
                  format(EASY, HARD, IMPOSSIBLE))

            difficult_mode = input("Please choose 1 difficulty.\n"
                                   ">>> ").upper()
            print()

            if difficult_mode == "1" or \
                difficult_mode == "2" or \
                difficult_mode == "3" or \
                difficult_mode == "EASY" or \
                difficult_mode == "HARD" or \
               difficult_mode == "IMPOSSIBLE":

                valid = True

                if difficult_mode == "1" or difficult_mode == "EASY":
                    mistakes = EASY
                    print("You are allowed to have {} wrong!".format(EASY))
                    time.sleep(1)

                elif difficult_mode == "2" or difficult_mode == "HARD":
                    mistakes = HARD
                    print("You are allowed to have {} wrong!".format(HARD))
                    time.sleep(1)

                elif difficult_mode == "3" or difficult_mode == "IMPOSSIBLE":
                    mistakes = IMPOSSIBLE
                    print("You are allowed to have only {} wrong!".
                          format(IMPOSSIBLE))
                    time.sleep(1)

                else:
                    print()
            else:
                print(error)

        except ValueError:
            print(error)

    return main_game()

# Main routines start here
def main_game():
    global correct_letter
    correct_letter = []
    wrong_letter = []

    import time

    print()
    print("THE WORD HAS {} LETTERS!".format(len(word)))

    global mistakes
    while mistakes > 0:
        time.sleep(1)
        print("You are allowed to have {} wrong left!".format(mistakes))
        time.sleep(1)
        guess = input("Type a letter and press 'Enter': ").upper()
        print()
        # 1 letter should be entered each guess
        if len(guess) == 1:
            if guess.isalpha():
                if guess in word:
                    # In case players enter a letter that they already had.
                    if guess not in wordlist:
                        print("You already have this letter!")
                    else:
                        correct_letter.append(guess)
                        wordlist.remove(guess)

                        # In case there are 2 or more same letters in the word
                        if wordlist.count(guess) > 0:

                            print("Awesome! There are {} '{}'s in the word!".
                                  format(word.count(guess), guess))

                            while wordlist.count(guess) > 0:
                                correct_letter.append(guess)
                                wordlist.remove(guess)

                        else:
                            print("Awesome! '{}' is in the word.".
                                  format(guess))
                    print()
                else:
                    if guess in wrong_letter:
                        print("You have already guessed this letter!")

                    else:
                        print("Sorry, '{}' is not in the word.".format(guess))
                        wrong_letter.append(guess)
                        mistakes -= 1
                    print()
                time.sleep(1)
                # Let players know what letters they have guessed so far.
                print("The letters you have guessed so far are:")
                print("Correct letters: {}\n"
                      "Wrong letters: {}".format(correct_letter, wrong_letter))
                print()
            else:
                mistakes -= 1
                print("Please enter A LETTER!")
                print()
        else:
            if guess == word:
                if difficult_mode == "3" or difficult_mode == "IMPOSSIBLE":
                    print("Amazing! You got the word without any wrong!\n"
                      "Congratulations!")
                else:
                    print("Congratulations! You won!")
                print()
                return play_again()
            else:
                mistakes -= 1
                print("Please enter ONE LETTER!")
                print()

        # If they get all the letters in the word, break the loop.
        global word_guess, confirm
        if len(correct_letter) == len(word):
            word_guess = 'Y'
            confirm = 'Y'
            break
        else:
            # If players get 3 or more correct letters
            # Ask them if they want to guess the word.
            if len(correct_letter) >= 3:
                time.sleep(1)
                valid = False

                while not valid:
                    error = "Please try again!"

                    try:
                        word_guess = input("Do you want to guess "
                                           "what the word is now? (Y/N)\n"
                                           ">>> ").upper()

                        if word_guess == "Y" or word_guess == "YES":
                            confirm = input("You will not be able to "
                                            "guess anymore letters!\n"
                                            "Do you wish to continue? (Y/N)\n"
                                            ">>> ").upper()

                            if confirm == "Y" or confirm == "YES":
                                valid = True
                                return guess_word()

                            elif confirm == "N" or confirm == "NO":
                                valid = True

                            else:
                                print(error)

                        elif word_guess == "N" or word_guess == "NO":
                            valid = True

                        else:
                            print(error)

                    except ValueError:
                        print(error)
                print()

    # Let them guess what the word is when they have got all the letters.
    if len(correct_letter) == len(word):
        return guess_word()

    # Print game over if they didn't get all the letters.
    else:
        print("GAME OVER!\n"
              "You didn't get all letters in the word.\n"
              "The word is: '{}'.\n"
              "Good luck next time!".format(word))
        return play_again()

# If players get all the letters in the word
# Let them have only 1 chance to guess the word
def guess_word():
    global guessed_word

    if len(correct_letter) == len(word):
        chance = 1

    # If they don't get all the letters, let them have 3 chances
    else:
        chance = 3

    while chance > 0:
        print("THE WORD HAS {} LETTERS!".format(len(word)))
        if word_guess == "Y" and confirm == "Y":
            guessed_word = input("Correct letters you got so far are: {}\n"
                                 "Can you guess what the word is?\n"
                                 ">>> ".format(correct_letter)).upper()

        else:
            guessed_word = input("You got all the letters in the word: {}\n"
                                 "Can you guess what the word is?\n"
                                 ">>> ".format(correct_letter)).upper()


        if guessed_word == word:

            if difficult_mode == "3" or difficult_mode == "IMPOSSIBLE":
                print("Amazing! You got the word without any wrong!\n"
                      "Congratulations!")

            else:
                print("Congratulations! You won!")

            break

        else:
            chance -= 1

            if chance > 0:
                print("Try again, I know you can get it this time!")

        # Print game over if they couldn't tell what the word was
    if guessed_word != word:

        print("GAME OVER!\n"
              "You couldn't tell what the word was!\n"
              "The word is: {}\n"
              "Good luck next time!".format(word))

        return play_again()

    else:
        return play_again()

# Play again function
def play_again():
    valid = False

    while not valid:
        error = "Please try again!"

        try:
            play_again = input("Do you want to play again? (Y/N): ").upper()

            if play_again == "Y" or play_again == "YES":
                valid = True
                print("=" * 50)
                return word_to_guess()

            elif play_again == "N" or play_again == "NO":
                valid = True
                print("Thank you for playing!")

            else:
                print(error)

        except ValueError:
            print(error)

word_to_guess()
