class room:
    def __init__(self, r, c): # r = row, c = col
        self.r = r
        self.c = c
'''
    1       2       3   
1   1,1     2,1     3,1 
2   1,2     2,2     3,2
3   1,3     2,3     3,3


'''
global queueList
queueList = []
def floodFill(r, c, color):
    queueList.append(room(r, c))
    

with open('theCastle/castle.in', 'r') as infile:
    lines = infile.readlines()
    data = []
    for line in lines:
        row = [int(x) for x in line.strip().split(" ")]
        data.append(row)

m = data[0][0]
n = data[0][1]

roomData = data[1:]

