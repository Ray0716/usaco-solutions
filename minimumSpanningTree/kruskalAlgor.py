class node:
    def __init__(self, row, col, weight):
        self.row = row
        self.col = col
        self.weight = weight

# IMPORTATN
# this actualy is not a node it's start, end and weight for the edge


def canReach(start, end, graph): # checks if you can reach a node from anotehr node
    # start and end is ints
    queue = [] # quere for BFS
    states = [0 for _ in range(n)]
    # states checks if we accessed any end node yet, to be used later in function

    queue.append(start)
    # appending first node to check into queue (BFS search the tree)
    states[start] = 1

    while len(queue) != 0:
        current = queue[0]
        queue.pop(0)
        if current == end:
            return True
        for endNode in range(len(graph)):
            if finalPath[current][endNode] > 0 and states[endNode] != 1:
                queue.append(endNode)
                states[endNode] = 1
    return False


graph = [
    [-1, 12, 18, -1, 17, -1],
    [12, -1, 10, 3, -1, 5],
    [18, 10, -1, -1, 21, 11], 
    [-1, 3, -1, -1, -1, 8],
    [17, -1, 21, -1, -1, 16], 
    [-1, 5, 11, 8, 16, -1]
]

# graph is 2d aray
# where: row = start, col = end, value = weight

n = 0
for row in graph:
    for col in row:
        if col != -1:
            n += 1
# n is # of nodes
print(f"n = {n}")


pathWeightList = []
pathWeightList.append(node(1, 3, 3))
pathWeightList.append(node(1, 5, 5))
pathWeightList.append(node(0, 4, 7))
pathWeightList.append(node(3, 5, 8))
pathWeightList.append(node(1, 2, 10))
pathWeightList.append(node(2, 5, 11))
pathWeightList.append(node(0, 1, 12))
pathWeightList.append(node(4, 5, 16))
pathWeightList.append(node(0, 2, 18))
pathWeightList.append(node(2, 4, 21))

'''
for row in range(len(graph)):
    for col in range(len(graph[0])):
        pathWeightList.append(node(row, col, graph[row][col]))
# appending node objects

# pathWeightList.sort(node.weight)
pathWeightList.sort(key=lambda x: x.weight)
'''

global finalPath
finalPath = [[0 for _ in range(len(graph))] for _ in range(len(graph[0]))]

for node in pathWeightList:
    if not canReach(node.row, node.col, graph):
        print("not")
        finalPath[node.row][node.col] = node.weight
        finalPath[node.col][node.row] = node.weight

for x in finalPath:
    print(x)


'''
Kruskal
'''