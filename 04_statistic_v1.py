def statistics(attempt, mistakes):

    stats_list = []
    percentage = attempt/mistakes
    stats_list.append(attempt)
    stats_list.append(mistakes)
    stats_list.append(round(percentage,2))
    print(stats_list)
statistics(2,7)
