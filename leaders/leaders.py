n = int(input())
pairs = 0
cowString = ([*input()])
lists = ([*input().split()])
inLists = [int(x) for x in lists]
lists = [0 for _ in range(len(inLists))]
# either G or H leader will contain all of its cows
# just count how many g's contain the leader or all H
for x in range(len(inLists)):
    lists[x] = cowString[x:inLists[x]]

letterList = lists
numLists = inLists

indexFirstG = cowString.index("G") # at least one of these is a leader guarenteed
indexFirstH = cowString.index("H")

howManyG = cowString.count("G")
howManyH = cowString.count("H")

firstGLeader = 0
fgl = False
firstHLeader = 0
fhl = False

reversedCowString = cowString[::-1]
indexLastG = len(cowString) - reversedCowString.index("G")
indexLastH = len(cowString) - reversedCowString.index("H")

if numLists[indexFirstG] >= indexLastG:
    firstGLeader = indexFirstG
    fgl = True
if numLists[indexFirstH] >= indexLastH:
    firstHLeader = indexFirstH
    fhl = True
if (fgl and fhl) == True:
    pairs = 1
    print(pairs)
    quit()


# if first g is leader, check all H and see which ones contain the G leader
if fgl:
    for x in range(indexFirstG): # if an H before first G(leader) contains it then it could also be a lweader
        if cowString[x] == "H" and x != indexFirstH:
            if numLists[x] >= indexFirstG:
                pairs += 1


if fhl:
    for x in range(indexFirstH):
        if cowString[x] == "G" and x != indexFirstG:
            if numLists[x] >= indexFirstH:
                pairs += 1


print(pairs)