def changeDir(dir):
    if dir == "R":
        return "L"
    else:
        return "R"
    
def count_lists_with_minus_one(list_of_lists):
    count = 0
    for sublist in list_of_lists:
        if sublist[0] == -1:
            count += 1
    return count

ns = [int(x) for x in input().split()]
n = ns[0]
s = ns[1]
numberLine = []
for _ in range(n):
    numberLine.append([int(x) for x in input().split()])

bessieLocation = s
bessieDirection = "R"
bessiePower = 1

jumpLog = []

if numberLine[bessieLocation - 1][0] == 0:
    #if she start on a jump pad
    bessieDirection = changeDir(bessieDirection) # chaNGE drir
    bessiePower += numberLine[bessieLocation - 1][1] # update power
elif numberLine[bessieLocation - 1][0] == 1: # if she start on target
    if numberLine[bessieLocation - 1][1] <= bessiePower:
        numberLine[bessieLocation - 1][0] = -1 # -1 denotes broken target


while (bessieLocation in range(1, n+1) and [bessieLocation, bessieDirection, bessiePower] not in jumpLog):
    jumpLog.append([bessieLocation, bessieDirection, bessiePower])
    #print(jumpLog)
    
    # while not (bessie inside line OR bessie infinite)
    # this is main simluation
    # first, make her jump
    # then, do stuff baseed on her current status
    if bessieDirection == "R":
        bessieLocation += bessiePower
    else:
        bessieLocation -= bessiePower

    


    if (bessieLocation in range(1, n+1) and [bessieLocation, bessieDirection, bessiePower] not in jumpLog):
        if numberLine[bessieLocation - 1][0] == 0: # if she lands on jump pad
            bessiePower += numberLine[bessieLocation - 1][1] # add power
            bessieDirection = changeDir(bessieDirection)
        elif numberLine[bessieLocation - 1][0] == 1: # if she land on target
            if bessiePower >= numberLine[bessieLocation - 1][1]:
                numberLine[bessieLocation - 1][0] = -1 # -1 denotes broken target
    else:
        break


#print(numberLine)
print(count_lists_with_minus_one(numberLine))
