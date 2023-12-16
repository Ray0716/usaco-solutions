with open('speeding.in', 'r') as inFile:
    nm = [int(x) for x in inFile.readline().split()]
    n = nm[0]
    m = nm[1]
    road = []
    bessieSpeeds = []
    for x in range(n):
        road.append([int(x) for x in inFile.readline().split()])
    for y in range(m):
        bessieSpeeds.append([int(y) for y in inFile.readline().split()])

changesRoad = []
changesBessie = []
roadDistance = 0
bessieDistance = 0

bessieOverSpeeds = []




#print(road)
#print(bessieSpeeds)
for x in range(len(road)):
    roadDistance += road[x][0]
    changesRoad.append(roadDistance - 1)
#print(changesRoad)

for y in range(len(bessieSpeeds)):
    bessieDistance += bessieSpeeds[y][0]
    changesBessie.append(bessieDistance - 1)
#print(changesBessie)

checkpoints = changesRoad + changesBessie
checkpoints.sort()


bessieSpeedMap = [0 for x in range(100)]
roadSpeedMap = [0 for x in range(100)]
for x in range(len(changesBessie)):
    if x == 0:
        bessieSpeedMap[0:changesBessie[x]+1] = [bessieSpeeds[x][1]] * len(bessieSpeedMap[0:changesBessie[x]+1])
    else:
        bessieSpeedMap[changesBessie[x-1]:changesBessie[x]] = [bessieSpeeds[x][1]] * len(bessieSpeedMap[changesBessie[x-1]:changesBessie[x]])

for x in range(len(changesRoad)):
    if x == 0:
        roadSpeedMap[0:changesRoad[x]+1] = [road[x][1]] * len(roadSpeedMap[0:changesRoad[x]+1])
    else:
        roadSpeedMap[changesRoad[x-1]:changesRoad[x]] = [road[x][1]] * len(roadSpeedMap[changesRoad[x-1]:changesRoad[x]])

#print(checkpoints)
#print(bessieSpeedMap)
#print(roadSpeedMap)

for place in checkpoints:
    bessieOverSpeeds.append(bessieSpeedMap[place] - roadSpeedMap[place])

#print(bessieOverSpeeds)
with open('speeding.out', 'w') as outFile:
    if n == 1 and m == 1:
        outFile.write(str(abs(bessieSpeeds[0][1] - road[0][1])))
    else:
        outFile.write(str(max(bessieOverSpeeds)))
