#
import pandas as pd

replacement_list= [["a","ā"],["e","ē"],["i","ī"],["o","ō"],["u","ū"]]
list2 = []
df = pd.read_csv('../Maori Words.csv')
Word_database = df.values.tolist()
print("The contents of the above file is as follows:")

for i in range (len(Word_database)):
    for g in range (len(replacement_list)-1):
        if Word_database[i][3] == replacement_list[g][0] and "?" in Word_database[i][1]:
            Word_database[i][1] = Word_database[i][1].replace("?",replacement_list[g][1])
    print(Word_database[i])
def spliting_function(list_needed):
    for g in range (len(list_needed)):
        list2.append([i for i in list_needed[g][1]])
spliting_function(Word_database)
print(list2)
