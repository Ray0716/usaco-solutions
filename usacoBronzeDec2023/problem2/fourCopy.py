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

#print(rangesOfOnes)
days = []
for index in range(len(rangesOfOnes)):
    if index == 0 or index == len(rangesOfOnes) - 1:
        if rangesOfOnes[index] % 2 == 0:
            d = (rangesOfOnes[index]/2) - 1
        else:
            d = (rangesOfOnes[index]-1) / 2
        days.append(min(rangesOfOnes[index]-1, d))

minDays = min(days)
for x in range(len(rangesOfOnes)):
    rangesOfOnes[x] -= minDays

print(int(sum(rangesOfOnes)))