'''def checkHowManyOtherElementsIsInRange(indexOfElement, list, k):
    result = []

    k = (min(list) + k) - (max(list) - k) 
    return 0'''

with open('diamond.in', 'r') as inFile:
    nk = [int(x) for x in inFile.readline().split()]
    n, k = nk[0], nk[1]
    data = []
    for x in range(n):
        data.append(int(inFile.readline()))

#print(f"n:{n}, k:{k}, datas:{data}")

goodDiamonds = []
for diamondIndex in range(len(data)):
    goodDiamondsForThisDiamond = 0
    rangeStart = data[diamondIndex] - k
    rangeEnd = data[diamondIndex] + k
    for d in data:
        if data[diamondIndex] <= d <= rangeEnd:
            goodDiamondsForThisDiamond += 1
    goodDiamonds.append(goodDiamondsForThisDiamond)
    #print(f"rsta:{rangeStart}, ren:{rangeEnd}, diamon:{data[diamondIndex]}, good:{goodDiamondsForThisDiamond}")


#print(goodDiamonds)


with open('diamond.out', 'w') as outFile:
    if sum(data) == data[0] * len(data):
        outFile.write(str(len(data)))
    outFile.write(str((max(goodDiamonds))))
