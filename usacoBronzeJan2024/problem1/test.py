def majorityCheck(list):
    possibleWinners = []
    if len(list) == 2:
        return [-1]
    for startIndex in range(len(list) - 2):
        endIndex = startIndex + 3
        window = list[startIndex:endIndex] # v is the 3 length window
        uniqueWindow = [x for x in set(window)]
        if len(uniqueWindow) == 1: # all one element
            possibleWinners.append(uniqueWindow[0])
        elif len(uniqueWindow) == 3: # all didfferent
            pass
        elif window.count(uniqueWindow[0]) == 2:
            possibleWinners.append(uniqueWindow[0])
        elif window.count(uniqueWindow[1]) == 2:
            possibleWinners.append(uniqueWindow[1])
    possibleWinners = [x for x in set(possibleWinners)]
    if len(possibleWinners) == 0:
        possibleWinners.append(-1)

    return possibleWinners

print(majorityCheck([1, 2, 3, 1, 2, 3, 3]))