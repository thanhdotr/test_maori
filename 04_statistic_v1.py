"""Component 4- Statistic. This takes the number of attempts and mistake and
create a statistic (percentage for each player) in the game. """
def statistics(attempt,word_length):

    stats_list = []
    #attempt is the times you make mistake while word length is
    # the number of letter in that word
    percentage = 1 - (attempt)/word_length
    stats_list.append(attempt)
    stats_list.append(word_length)
    stats_list.append(round(percentage,2))
    print(stats_list)
    for i in range (len(stats_list)):
        print(f"Player {i} got {attempt} in a word with {word_length} letter")
statistics(2,6)
statistics(2,3)
statistics(1,2)
statistics(1,6)
statistics(5,6)
