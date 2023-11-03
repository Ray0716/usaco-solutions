class node:
    def __init__(self, row, col):
        self.row = row
        self.col = col


graph = [
    [0, 20, 15, -1, -1, -1],
    [2, 0, 4, -1, 10, 30],
    [-1, -1, 0, -1, -1, 10],
    [-1, -1, -1, 0, -1, -1],
    [-1, -1, -1, 15, 0, 10],
    [-1, -1, -1, 4, -1, 0]
]

states = [0 for _ in range(len(graph))]
distance = [0 for _ in range(len(graph))]
