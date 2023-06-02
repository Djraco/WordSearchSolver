import math
from textwrap import wrap


words = ['BEAR', 'FROG', 'GIRAFFE', 'GOAT', 'LION', 'PANDA', 'PENGUIN', 'TIGER', 'TOAD']
raw = ("PUROVPRSESEAMATGNNGDEOODGAIBRAWOUWTKTTNOILYMFROGN")
size = int(math.sqrt(len(raw)))
found = []


def checkRight(word):
    table = wrap(raw, size)
    for x in table:
        if x.find(word) != -1:
            return(str(x.find(word)) + ',' + str(table.index(x)))


def checkLeft(word):
    word = word[:: -1]
    table = wrap(raw, size)
    for x in table:
        if x.find(word) != -1:
            return(str(x.find(word)+len(word)-1) + ',' + str(table.index(x)))


def checkUp(word):
    return


def checkDown(word):
    return


def findWords():
    for x in words:
        if checkRight(x) != None:
            found.append(x + ': ' + str(checkRight(x)) + ' (Right)')

        if checkLeft(x) != None:
            found.append(x + ': ' + str(checkLeft(x)) + ' (Left)')

    return(found)


print(findWords())


