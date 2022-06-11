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
