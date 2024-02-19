def distance(x1, y1, x2, y2):
    return (x2-x1)**2 + (y2-y1)**2

n = int(input())
xCoords = [int(x) for x in input().split()]
yCoords = [int(x) for x in input().split()]

distances = []

for firstPointIndex in range(len(xCoords)):
    for secondPointIndex in range(firstPointIndex+1, n):
        if [xCoords[firstPointIndex], yCoords[firstPointIndex]] != [xCoords[secondPointIndex], yCoords[secondPointIndex]]:
            #print([xCoords[firstPointIndex], yCoords[firstPointIndex]])
            #print([xCoords[secondPointIndex], yCoords[secondPointIndex]])
            distances.append(distance(xCoords[firstPointIndex], yCoords[firstPointIndex], xCoords[secondPointIndex], yCoords[secondPointIndex]))

print(max(distances))

