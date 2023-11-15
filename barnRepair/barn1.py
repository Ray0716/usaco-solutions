with open('barnRepair/barn1.in', 'r') as infile:
    lines = infile.readlines()
    otherData = lines[0].split()
    del lines[0]
    otherData = [int(x) for x in otherData]    

    occupiedStalls = [int(s.replace('\n', '')) for s in lines]

    #print(otherData)
    #print(stalls)

    maxBoards = otherData[0]
    numStalls = otherData[1]
    numCows = otherData[2]


if maxBoards == 1:
    with open('barnRepair/barn1.out', 'w') as outFile:
        outFile.write(str(numStalls - ((occupiedStalls[0] - 1) + (numStalls - occupiedStalls[-1]))))

spans = []
for index in range(len(occupiedStalls) - 1):
    spans.append((occupiedStalls[index+1] - occupiedStalls[index]) - 1)
    # making span list (span inbetween occupied stalls)


print(occupiedStalls)
print(f"wt spans: {spans}")

coveredStalls = numStalls

sortedSpans = sorted(spans, reverse=True)
coveredStalls -= sum(sortedSpans[:maxBoards-1]) # subtracting gaps, sorted spans is for the greatest X gaps
#print(sortedSpans[:maxBoards])
#print(sum(sortedSpans[:maxBoards]))

#print(coveredStalls)
print(spans)
coveredStalls -= (occupiedStalls[0] - 1)
coveredStalls -= (numStalls - occupiedStalls[-1])
print(coveredStalls)

with open('barnRepair/barn1.out', 'w') as outFile:
    outFile.write(str(coveredStalls))

