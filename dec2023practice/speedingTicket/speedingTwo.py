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


#print(road)
#print(bessieSpeeds)
for x in range(len(road)):
    roadDistance += road[x][0]
    changesRoad.append([roadDistance, road[x][1]])
#print(changesRoad)

for y in range(len(bessieSpeeds)):
    bessieDistance += bessieSpeeds[y][0]
    changesBessie.append([bessieDistance, bessieSpeeds[y][1]])
#print(changesRoad)
#print(changesBessie)

roadMap = []
bessieMap = []

for x in range(len(changesRoad)):
    for _ in range(road[x][0]):
        roadMap.append(changesRoad[x][1])
for y in range(len(changesBessie)):
    for _ in range(bessieSpeeds[y][0]):
        bessieMap.append(changesBessie[y][1])

#print(roadMap)
#print(bessieMap)
speeding = []
for i in range(len(roadMap)):
    speeding.append(bessieMap[i] - roadMap[i])

with open('speeding.out', 'w') as outFile:
    #if n == 1 and m == 1:
   #     outFile.write(str(abs(bessieSpeeds[0][1] - road[0][1])))
   # else:
   outFile.write(str(max(speeding)))
