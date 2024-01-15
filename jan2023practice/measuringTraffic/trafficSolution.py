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
    

roadSegments = []
with open("traffic.in", 'r') as infile:
    n = int(infile.readline())
    for x in range(n):
        data = infile.readline().split()
        data[1] = int(data[1])
        data[2] = int(data[2])
        roadSegments.append(roadSegment(data[0], data[1], data[2]))



#print(findMiddleRange(roadSegments[find_longest_none_run(roadSegments)[0]:find_longest_none_run(roadSegments)[1] + 1]))

beforeHighway = roadSegment("none", -1001, 1001)

afterHighway = roadSegment("none", -1001, 1001)

for roadSegIndex in range(0, len(roadSegments)):
    # calc before
    if roadSegments[roadSegIndex].type == "none":
        #afterHighway.sub(roadSegments[roadSegIndex].lowRange, roadSegments[roadSegIndex].highRange)
        if roadSegments[roadSegIndex].lowRange > afterHighway.lowRange:
            afterHighway.lowRange = roadSegments[roadSegIndex].lowRange

        if roadSegments[roadSegIndex].highRange < afterHighway.highRange:
            afterHighway.highRange = roadSegments[roadSegIndex].highRange

    
    if roadSegments[roadSegIndex].type == "on":
        #afterHighway.add(roadSegments[roadSegIndex].lowRange, roadSegments[roadSegIndex].highRange)
        afterHighway.lowRange += roadSegments[roadSegIndex].lowRange
        afterHighway.highRange += roadSegments[roadSegIndex].highRange

    if roadSegments[roadSegIndex].type == "off":
        #afterHighway.add(roadSegments[roadSegIndex].lowRange, roadSegments[roadSegIndex].highRange)
        afterHighway.lowRange -= roadSegments[roadSegIndex].highRange
        afterHighway.highRange -= roadSegments[roadSegIndex].lowRange

for roadSegIndex in range(len(roadSegments)-1, -1, -1):
    # calc before
    if roadSegments[roadSegIndex].type == "none":
        #beforeHighway.sub(roadSegments[roadSegIndex].lowRange, roadSegments[roadSegIndex].highRange)
        if roadSegments[roadSegIndex].lowRange > beforeHighway.lowRange:
            beforeHighway.lowRange = roadSegments[roadSegIndex].lowRange

        if roadSegments[roadSegIndex].highRange < beforeHighway.highRange:
            beforeHighway.highRange = roadSegments[roadSegIndex].highRange

    
    if roadSegments[roadSegIndex].type == "on":
        #beforeHighway.add(roadSegments[roadSegIndex].lowRange, roadSegments[roadSegIndex].highRange)
        
        beforeHighway.lowRange -= roadSegments[roadSegIndex].highRange
        beforeHighway.highRange -= roadSegments[roadSegIndex].lowRange

    if roadSegments[roadSegIndex].type == "off":
        #beforeHighway.add(roadSegments[roadSegIndex].lowRange, roadSegments[roadSegIndex].highRange)
        
        beforeHighway.lowRange += roadSegments[roadSegIndex].lowRange
        beforeHighway.highRange += roadSegments[roadSegIndex].highRange



#print(f"{beforeHighway.type}, {beforeHighway.lowRange}, {beforeHighway.highRange}")

#print(f"{afterHighway.type}, {afterHighway.lowRange}, {afterHighway.highRange}")
if beforeHighway.lowRange < 0:
    beforeHighway.lowRange = 0

if afterHighway.lowRange < 0:
    afterHighway.lowRange = 0


with open("traffic.out", "w") as outFile:
    outFile.write(str(beforeHighway.lowRange))
    outFile.write(" ")
    outFile.write(str(beforeHighway.highRange))
    outFile.write("\n")
    outFile.write(str(afterHighway.lowRange))
    outFile.write(" ")
    outFile.write(str(afterHighway.highRange))