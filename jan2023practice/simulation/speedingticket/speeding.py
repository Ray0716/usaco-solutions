def returnSpeedMap(data):
    map = []
    for x in data:
        for c in range(x[0]):
            map.append(x[1])

    return map


with open('speeding.in', 'r') as infile:
    nm = [int(x) for x in infile.readline().split()]
    n = nm[0]
    m = nm[1]
    data = []

    for _ in range(n + m):
        data.append([int(x) for x in infile.readline().split()])

speeds = data[:n]
d = data[n:]
bessie = d

spMap = returnSpeedMap(speeds)
bMap = returnSpeedMap(bessie)

dMap = []
for x in range(100):
    dMap.append(bMap[x] - spMap[x])

with open('speeding.out', 'w') as outfile:
    if max(dMap) <= 0:
        outfile.write("0")
        quit()
    else:
        outfile.write(str(max(dMap)))
        quit()