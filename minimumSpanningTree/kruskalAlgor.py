class node:
    def __init__(self, row, col, weight):
        self.row = row
        self.col = col
        self.weight = weight

graph = [
    -1, 12, 18, -1, 17, -1,
    12, -1, 10, 3, -1, 5, 
    18, 10, -1, -1, 21, 11, 
    -1, 3, -1, -1, -1, 8, 
    17, -1, 21, -1, -1, 16, 
    -1, 5, 11, 8, 16, -1
]

pathWeightList = []
# this list has node objects

for row in range(n):
    for col in range(row, n):
        if graph[row][col] != -1:
            pathWeightList.append(node(row, col, graph[row][col]))

pathWeightList.sort(node.weight)

def canReach(start, end, graph):
    queue = [] # quere for BFS
    states = [for _ in range(n)]

'''
Kruskal:
1. make listof node objects
2. canreach function (make new 2d array and accesslist and states (colros) ad use BFS, if cur and k k is rthe destination and states is not accesed we ppend , states[k] is destination of the current edge)

'''