n = int(input())
data = [*input()]
data = [int(x) for x in data]

if all(data) is True:
    print(1)
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

days = min(rangesOfOnes)
if days == 1 or days == 2:
    days = 1
elif days % 2 == 0:
    days = (days / 2) - 1
elif days % 2 == 1:
    days = (days-1)/2

if days == 1:
    print(sum(rangesOfOnes))
    quit()

for spread in range(len(rangesOfOnes)):
    rangesOfOnes[spread] -= days * 2

# - -   -   -   -   -   -   -   -   -
'''startingCows = 0

for spread in rangesOfOnes:
    if spread % 2 == 0: #if even
        startingCows += 2
    elif spread % 2 == 1:
        startingCows += 1'''

print(sum(rangesOfOnes))




