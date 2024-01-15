class roadSegment:
    def __init__(self, type, lowRange, highRange):
        self.type = type #on, off or none
        self.lowRange = lowRange
        self.highRange = highRange
    
    def add(self, otherSegLow, otherSegHigh):
        self.lowRange = self.lowRange + otherSegHigh
        self.highRange = self.highRange + otherSegLow
    
    def sub(self, otherSegLow, otherSegHigh):
        self.lowRange = self.lowRange - otherSegHigh
        self.highRange = self.highRange - otherSegLow
    
def findMiddleRange(listOfRoadSegments):
    return [max(listOfRoadSegments, key=lambda x: x.lowRange).lowRange, min(listOfRoadSegments, key=lambda x: x.highRange).highRange]

def find_longest_none_run(segments):
    current_run = []
    longest_run = []

    for index, segment in enumerate(segments):
        if segment.type == "none":
            current_run.append(index)
        else:
            if len(current_run) > len(longest_run):
                longest_run = current_run
            current_run = []

    # Check for the last run
    if len(current_run) > len(longest_run):
        longest_run = current_run

    return [min(longest_run), max(longest_run)]

roadSegments = []
with open("traffic.in", 'r') as infile:
    n = int(infile.readline())
    for x in range(n):
        data = infile.readline().split()
        data[1] = int(data[1])
        data[2] = int(data[2])
        roadSegments.append(roadSegment(data[0], data[1], data[2]))



straightPartOfHighway = find_longest_none_run(roadSegments)

longestRunStart = find_longest_none_run(roadSegments)[0]
longestRunEnd = find_longest_none_run(roadSegments)[1]

#print(findMiddleRange(roadSegments[find_longest_none_run(roadSegments)[0]:find_longest_none_run(roadSegments)[1] + 1]))

beforeHighway = roadSegment("none", findMiddleRange(roadSegments[find_longest_none_run(roadSegments)[0]:find_longest_none_run(roadSegments)[1] + 1])[0], findMiddleRange(roadSegments[find_longest_none_run(roadSegments)[0]:find_longest_none_run(roadSegments)[1] + 1])[1])

afterHighway = roadSegment("none", findMiddleRange(roadSegments[find_longest_none_run(roadSegments)[0]:find_longest_none_run(roadSegments)[1] + 1])[0], findMiddleRange(roadSegments[find_longest_none_run(roadSegments)[0]:find_longest_none_run(roadSegments)[1] + 1])[1])

for roadSegIndex in range(longestRunStart, -1, -1):
    # calc before
    if roadSegments[roadSegIndex].type == "on":
        beforeHighway.sub(roadSegments[roadSegIndex].lowRange, roadSegments[roadSegIndex].highRange)
    if roadSegments[roadSegIndex].type == "off":
        beforeHighway.add(roadSegments[roadSegIndex].lowRange, roadSegments[roadSegIndex].highRange)

for roadSegIndex in range(longestRunEnd, len(roadSegments)):
    # calc before
    if roadSegments[roadSegIndex].type == "on":
        afterHighway.add(roadSegments[roadSegIndex].lowRange, roadSegments[roadSegIndex].highRange)
    if roadSegments[roadSegIndex].type == "off":
        afterHighway.sub(roadSegments[roadSegIndex].lowRange, roadSegments[roadSegIndex].highRange)



#print(f"{beforeHighway.type}, {beforeHighway.lowRange}, {beforeHighway.highRange}")

#print(f"{afterHighway.type}, {afterHighway.lowRange}, {afterHighway.highRange}")

with open("traffic.out", "w") as outFile:
    outFile.write(str(beforeHighway.lowRange))
    outFile.write(" ")
    outFile.write(str(beforeHighway.highRange))
    outFile.write("\n")
    outFile.write(str(afterHighway.lowRange))
    outFile.write(" ")
    outFile.write(str(afterHighway.highRange))