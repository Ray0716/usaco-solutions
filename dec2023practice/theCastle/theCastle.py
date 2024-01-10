with open('theCastle/castle.in', 'r') as infile:
    lines = infile.readlines()
    data = []
    for line in lines:
        row = [int(x) for x in line.strip().split(" ")]
        data.append(row)

m = data[0][0] # NUM OF COLUMNS (|)
n = data[0][1] # NUM OF ROWS    (-)

roomData = data[1:]

print(roomData)

# ------------------------------------------------

class room:
    def __init__(self, row, col): # r = row, c = col
        self.row = row
        self.col = col
'''
    1       2       3     (M, col)
1   1,1     2,1     3,1 
2   1,2     2,2     3,2
3   1,3     2,3     3,3
(N, row)

denoted as (row, col)

OUTPUT:
Line 1 - 

'''
color = 1

accessList = [[0 for _ in range(m+1)] for _ in range(n+1)]

def floodFill(row, col, color): # floods one room with one color, start point is r,c
    queueList = []
    queueList.append(room(row, col))

    while len(queueList) != 0:
        node = room(queueList[0].row, queueList[0].col)
   
        r = queueList[0].row
        c = queueList[0].col
        print(f"row: {r}, col:{c}, color:{color}")
        accessList[r][c] = color
        queueList.pop(0)

        if (roomData[r][c] & 1 == 0) and (accessList[r][c-1] == 0): # no wall west
            queueList.append(room(r, c-1))

        if (roomData[r][c] & 2 == 0) and (accessList[r-1][c] == 0): # no wall north
            queueList.append(room(r-1, c))

        if (roomData[r][c] & 4 == 0) and (accessList[r][c+1] == 0): # no wall east
            queueList.append(room(r, c+1))

        if (roomData[r][c] & 8 == 0) and (accessList[r+1][c] == 0): # no wall south
            queueList.append(room(r+1, c))



for a in range(n+1):
    if a == 0:
        continue
    for b in range(m+1):
        if b == 0:
            continue
        if accessList[a-1][b-1] == 0:
            floodFill(a-1, b-1, color)
            color += 1

for line in accessList:
    print(line)


