with open('theCastle/castle.in', 'r') as infile:
    lines = infile.readlines()
    data = []
    for line in lines:
        row = [int(x) for x in line.strip().split(" ")]
        data.append(row)

m = data[0][0]
n = data[0][1]

roomData = data[1:]

# ------------------------------------------------

class room:
    def __init__(self, r, c): # r = row, c = col
        self.r = r
        self.c = c
'''
    1       2       3     (M)
1   1,1     2,1     3,1 
2   1,2     2,2     3,2
3   1,3     2,3     3,3
(N)

OUTPUT:
Line 1 - 

'''
color = 1

accessList = [[0 for _ in range(n)] for _ in range(m)]

def floodFill(row, col, color): # floods one room with one color
    queueList = []
    queueList.append(room(row, col))

    while len(queueList) != 0:
        node = room(queueList[0].row, queueList[0].col)
        queueList.pop(0)

        if (roomData[row][col] & 1 == 0) and (accessList[row][col] == 0): # no wall east
            





