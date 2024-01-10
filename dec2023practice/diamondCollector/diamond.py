with open('diamondCollector/diamond.in', 'r') as inFile:
    nk = [int(x) for x in inFile.readline().split()]
    n, k = nk[0], nk[1]
    data = []
    for x in range(n):
        data.append(int(inFile.readline()))

rangeList = [0 for x in range(len(data) - k)]
for diamondIndex in range(len(data) - k):
    # range: dindex, dindex+k
    rangeStart = diamondIndex
    rangeEnd = diamondIndex + k
    diamondRange = data[rangeStart:rangeEnd + 1]

    rangeList.append(sum(diamondRange))
    




with open('diamondCollector/diamond.out', 'w') as outFile:
    outFile.write("aksruedfghly poopoo peepee heheheha ")
