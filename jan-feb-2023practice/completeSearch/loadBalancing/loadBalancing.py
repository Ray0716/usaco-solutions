with open('balancing.in', 'r') as infile:
    nb = [int(x) for x in infile.readline().split()]
    n = nb[0]
    b = nb[1]
    points = []
    xPoints = []
    yPoints = []
    for _ in range(n):
        thisPoint = [int(x) for x in infile.readline().split()]
        points.append(thisPoint)
        xPoints.append(thisPoint[0])
        yPoints.append(thisPoint[1])

maxPointsInQuad = []
for x in range(0, max(xPoints), 2):
    for y in range(0, max(yPoints), 2):
        UL = 0
        UR = 0
        LL = 0
        LR = 0
        for point in points:
            if point[1] < y:
                if point[0] < x:
                    LL += 1
                else:
                    LR += 1
            else:
                if point[0] < x:
                    UL += 1
                else:
                    UR += 1
        maxPointsInQuad.append(max(LL, LR, UL, UR))
with open('balancing.out', 'w') as outfile:
    outfile.write(str(min(maxPointsInQuad)))