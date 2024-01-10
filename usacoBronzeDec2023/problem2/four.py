n = int(input())
data = [*input()]
data = [int(x) for x in data]

def find_second_minimum(lst):
    # Find the second minimum value by excluding the minimum
    min_value = min(lst)
    second_min_value = min(value for value in lst if value != min_value)

    return second_min_value

if all(data) is True:
    print("1")
    quit()

# determine rantges of 1's
# if length of ransghe is even, it is 2 cow (if it is 2, then it is 2)
# if odd, itr is 1 cow

rangesOfOnes = []
rangeLen = 0
zeroIsAfterRange = False
for cow in range(len(data)):
    if data[cow] == 1:
        rangeLen += 1
        zeroIsAfterRange = True
    elif data[cow] == 0 and zeroIsAfterRange == True:
        rangesOfOnes.append(rangeLen)
        rangeLen = 0
        zeroIsAfterRange = False
if data[-1] == 1:
    rangeLen = 0
    for cow in reversed(data):
        if cow == 0:
            break
        else:
            rangeLen += 1
    rangesOfOnes.append(rangeLen)

if len(rangesOfOnes) == 1:
    if rangesOfOnes[0] % 2 == 0:
        print("2")
        quit()
    else:
        print("1")
        quit()

days = []

for spreadIndex in range(len(rangesOfOnes)): # for each outbreak
    try:
        if (spreadIndex == 0 and data[0] == 1) and (spreadIndex+1 == len(rangesOfOnes) - 1 and data[-1] == 1):
            if rangesOfOnes[spreadIndex] == 1 or rangesOfOnes[spreadIndex - 1] == 1:
                print(sum(days))
                quit()
            elif rangesOfOnes[spreadIndex] == 2 or rangesOfOnes[spreadIndex - 1] == 2:
                days.append(1)
                continue
            days.append(rangesOfOnes[0] - 1) # assuming first cow is at edge
            if rangesOfOnes[spreadIndex] % 2 == 0:
                days.append((rangesOfOnes[spreadIndex]/2)-1)
            else:
                days.append((rangesOfOnes[spreadIndex]-1)/2)

            days.append(rangesOfOnes[spreadIndex+1] - 1) # assuming first cow is at edge
            if rangesOfOnes[spreadIndex+1] % 2 == 0:
                days.append((rangesOfOnes[spreadIndex+1]/2)-1)
            else:
                days.append((rangesOfOnes[spreadIndex+1]-1)/2)
    except:
        pass

    if spreadIndex == 0 and data[0] == 1:#first range
        if rangesOfOnes[spreadIndex] == 1:
            print(sum(days))
            quit()
        elif rangesOfOnes[spreadIndex] == 2:
            days.append(1)
            continue
        days.append(rangesOfOnes[0] - 1) # assuming first cow is at edge
        if rangesOfOnes[spreadIndex] % 2 == 0:
            days.append((rangesOfOnes[spreadIndex]/2)-1)
        else:
            days.append((rangesOfOnes[spreadIndex]-1)/2)

    elif spreadIndex == len(rangesOfOnes) - 1 and data[-1] == 1:# last range
        if rangesOfOnes[spreadIndex] == 1:
            print(sum(rangesOfOnes))
            quit()
        elif rangesOfOnes[spreadIndex] == 2:
            days.append(1)
            continue
        days.append(rangesOfOnes[spreadIndex] - 1) # assuming first cow is at edge
        if rangesOfOnes[spreadIndex] % 2 == 0:
            days.append((rangesOfOnes[spreadIndex]/2)-1)
        else:
            days.append((rangesOfOnes[spreadIndex]-1)/2)

    else: #normal range 
        if rangesOfOnes[spreadIndex] % 2 == 0:
            days.append((rangesOfOnes[spreadIndex]/2)-1)
        else:
            days.append((rangesOfOnes[spreadIndex]-1)/2)

minDay = min(days)
print(minDay)

for spread in range(len(rangesOfOnes)):
    if spread == 0 and data[0] == 1:
        rangesOfOnes[spread] -= minDay
    elif (spread == len(rangesOfOnes) - 1) and data[-1] == 1: # if spread on the edges we only take off days on one side assuiming starting cow is on the very end
        rangesOfOnes[spread] -= minDay
    else:
        rangesOfOnes[spread] = int(rangesOfOnes[spread] - (minDay * 2))
        
    if rangesOfOnes[spread] <= 0:
        rangesOfOnes[spread] = 0
    

#print("original:", rangesOfOnes)
print(int(sum(rangesOfOnes)))





