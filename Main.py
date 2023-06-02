import math
from textwrap import wrap


words = ['abc', 'lkji', 'dhl', 'iem']        
raw = ("abcdefghijklmnop")
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


def checkDown(word):
    table = wrap(raw, size)
    table_down = []
    for i in range(len(table[0])):
        downraw = ''
        for j in range(len(table)):
            downraw = downraw + (table[j][i])
        table_down.append(downraw)
    for x in table_down:
        if x.find(word) != -1:
            return(str(table_down.index(x)) + ',' + str(x.find(word)+len(word)-1))
checkDown('BEAR')

def checkUp(word):
    
    return


def findWords():
    for x in words:
        if checkRight(x) != None:
            found.append(x + ': ' + str(checkRight(x)) + ' (Right)')

        if checkLeft(x) != None:
            found.append(x + ': ' + str(checkLeft(x)) + ' (Left)')

        if checkDown(x) != None:
            found.append(x + ': ' + str(checkDown(x)) + ' (Down)')

    return(found)


print(findWords())

# # # # # # #
#     0 1 2 3
#
# 0   a b c d
# 1   e f g h
# 2   i j k l 
# 3   m n o p


# # # # # # #
#     0 1 2 3
#  
# 0   a e i m
# 1   b f j n
# 2   c g k o 
# 3   d h l p

#1) swap x and y (x,y = y,x)
#2) 
