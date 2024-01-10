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

days = min(rangesOfOnes)
#print(rangesOfOnes)
# we backtrack andf find the original cows by seeing the smallest infected patch
# the smallest patch is the number days

if days == 1 or days == 2:
    print(sum(rangesOfOnes))
    quit()
elif (rangesOfOnes[0] == days and data[0] == 1) or (rangesOfOnes[-1] == days and data[-1] == 1): # if the smallest infect group is on the edge
    #print("day on edge")

    days = days - 1

elif days % 2 == 0: #if even num of days since outbreak first astart (with initial cows)
    #print("even day")
    days = (days/2) - 1
elif days % 2 == 1:
    #print("opdd day")11
    days = (days-1)/2

days = int(days)


#print(rangesOfOnes)


if data[0] == 1 and data[-1] == 1: # if there are two outbreAKS on the edges
    if rangesOfOnes[0] == rangesOfOnes[-1] and rangesOfOnes[0] == min(rangesOfOnes):
        print("1")
        quit()
    else:
        if rangesOfOnes[0] > rangesOfOnes[-1] and rangesOfOnes[-1] == min(rangesOfOnes):
            days = min(rangesOfOnes[0]-1, rangesOfOnes[-1]-1)
        if rangesOfOnes[0] < rangesOfOnes[-1] and rangesOfOnes[0] == min(rangesOfOnes):
            days = min(rangesOfOnes[0]-1, rangesOfOnes[-1]-1)

elif data[0] == 1 and rangesOfOnes[0] == min(rangesOfOnes):# outbreak on left edge
    nextLargestRange = find_second_minimum(rangesOfOnes)
    eDays = rangesOfOnes[0] - 1
    otherDays = 0
    if nextLargestRange % 2 == 0: #if even num of days since outbreak first astart (with initial cows)
        #print("even day")
        otherDays = (nextLargestRange/2) - 1
    elif nextLargestRange % 2 == 1:
        #print("opdd day")11
        otherDays = (nextLargestRange-1)/2
    otherDays = int(otherDays)
    #print(eDays)
    #print(otherDays)
    days = min(eDays, otherDays)

elif data[-1] == 1 and rangesOfOnes[-1] == min(rangesOfOnes):# outbreak on rigth edge
    nextLargestRange = find_second_minimum(rangesOfOnes)
    eDays = rangesOfOnes[-1] - 1
    otherDays = 0
    if nextLargestRange % 2 == 0: #if even num of days since outbreak first astart (with initial cows)
        #print("even day")
        otherDays = (nextLargestRange/2) - 1
    elif nextLargestRange % 2 == 1:
        #print("opdd day")11
        otherDays = (nextLargestRange-1)/2
    otherDays = int(otherDays)
    #print(eDays)
    #print(otherDays)
    days = min(eDays, otherDays)
#print(f"days:{days}, ranges:{rangesOfOnes}")
#print(days)








for spread in range(len(rangesOfOnes)):
    if spread == 0 and data[0] == 1:
        rangesOfOnes[spread] -= days
    elif (spread == len(rangesOfOnes) - 1) and data[-1] == 1: # if spread on the edges we only take off days on one side assuiming starting cow is on the very end
        rangesOfOnes[spread] -= days
    else:
        rangesOfOnes[spread] = int(rangesOfOnes[spread] - (days * 2))
        
    if rangesOfOnes[spread] <= 0:
        rangesOfOnes[spread] = 0


#print("original:", rangesOfOnes)
print(sum(rangesOfOnes))





