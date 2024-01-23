with open('mowing.in', 'r') as infile:
    n = int(infile.readline())
    data = []
    for _ in range(n):
        temp = infile.readline().split()
        data.append([temp[0], int(temp[1])])


cellVisits = [] # log visited cells and times
fjPosition = [0, 0]
time = 0
cellVisits.append([0, 0, 0]) # first mowed cell is when he starts, [x, y, time]
for move in data: #move = ['N', 4]
    if move[0] == 'N':
        # fjPosition[1] += move[1]
        for x in range(move[1]): # make farmer john mow cells one at a time
            fjPosition[1] += 1
            time += 1
            cellVisits.append([fjPosition[0], fjPosition[1], time])
    if move[0] == 'E':
        for x in range(move[1]): # make farmer john mow cells one at a time
            fjPosition[0] += 1
            time += 1
            cellVisits.append([fjPosition[0], fjPosition[1], time])
    if move[0] == 'S':
        for x in range(move[1]): # make farmer john mow cells one at a time
            fjPosition[1] -= 1
            time += 1
            cellVisits.append([fjPosition[0], fjPosition[1], time])
    if move[0] == 'W':
        for x in range(move[1]): # make farmer john mow cells one at a time
            fjPosition[0] -= 1
            time += 1
            cellVisits.append([fjPosition[0], fjPosition[1], time])

# now iterasthe through cell visitss
# if two coords are equal, FJ revisits a cell
# append diffenece in time to a list, find min of list
timeDifferences = [] #amount of time it takes him to revisit cells
for coord in cellVisits:
    for comparedCoord in cellVisits:
        if coord == comparedCoord:
            continue
        if (coord[0] == comparedCoord[0]) and (coord[1] == comparedCoord[1]):
            # if coords match (he revisites)
            timeDifferences.append(max(coord[2], comparedCoord[2]) - min(coord[2], comparedCoord[2]))

with open('mowing.out', 'w') as outfile:
    if len(timeDifferences) == 0:
        outfile.write("-1")
        quit()
    else:
        outfile.write(str(min(timeDifferences)))