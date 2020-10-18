import math
alphab ="abcdefghijklmnopqrstuvwxyz"

words = ["pero", "ruchka", "bumaga"]
result = ''
if alphab[alphab.index(words[0][2])+1] != "z":
    result += alphab[alphab.index(words[0][2])+1]
else:
    result += "a"
if alphab[alphab.index(words[0][2])-1] != "z":
    result += alphab[alphab.index(words[0][2])-1]
else:
    result += "z"

if len(words[2])/2 != int(len(words[2])/2):
    if alphab[alphab.index(words[2][int(len(words[2])/2)])+1] == "z":
        result += "a"
    else:
        flwindex = int(len(words[2])/2)
        result += alphab[alphab.index(words[2][flwindex])+1]
else:
    if alphab[alphab.index(words[2][int(len(words[2])/2-1)])-1] != "a":
        result += alphab[alphab.index(words[2][int(len(words[2])/2-1)])-1]
    else:
        result += "z"

index = len(words[1]) + len(words[2])
if index > 26:
    index %= 26
result += alphab[index - 1]
print(result)




