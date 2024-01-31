def majorityCheck(list):
    counts = []
    if all(i == list[0] for i in list):
        return list[0]
    else:
        for element in set(list):
            counts.append([list.count(element), element])
        print(counts)
        for x in counts:
            #if x >= len(list)/2:
            if len(list) % 2 == 0:
                if x[0] >= len(list)/2 + 1:
                    return x[1]
            elif len(list) % 2 != 0:
                if x[0] >= (len(list)+1)/2:
                    return x[1]
    return -1

test = 0

def solve():
    numCows = int(input())
    favoriteHays = [int(x) for x in input().split()]
    for startIndex in range(numCows - 2):
        for endIndex in range(startIndex + 2, numCows):
            #print(startIndex, endIndex)
            majority = majorityCheck(favoriteHays[startIndex:endIndex])
            print(startIndex, endIndex, majority)
            favoriteHays[startIndex:endIndex + 1] = [majority] * len(favoriteHays[startIndex:endIndex + 1])

    print(favoriteHays)


n = int(input())

for _ in range(n):
    solve()