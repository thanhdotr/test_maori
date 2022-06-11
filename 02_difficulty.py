def main_function():
    easy = 6
    medium = 3
    hard = 2
    print(f"1 - Easy:  {easy} wrong attempts.\n"
                  f"2 - Medium:{medium} wrong attempts.\n"
                  f"3 - Hard: {hard} wrong attempts.")

    difficult_mode = input("Difficulties:\n"
                            "").upper()

    if difficult_mode == "1":
        mistakes = easy
        print("You are allowed to have {} wrong!".format(easy))

    elif difficult_mode == "2" :
        mistakes = medium
        print("You are allowed to have {} wrong!".format(medium))

    elif difficult_mode == "3" :
        mistakes = hard
        print("You are allowed to have only {} wrong!".
              format(hard))
    else:
        print(error)


def game_difficulty():

    global mistakes, difficult_mode, error
    # Set up difficulties

    input("Press 'Enter' to start: ")
    # Let the players choose one difficulty mode
    valid = False
    while not valid:
        error = "Please choose 1 in 3 difficulties!"
        try:
            main_function()
            valid = True

        except ValueError:
                print(error)

    return 'start the game'


print(game_difficulty())
