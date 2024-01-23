with open('jan2023practice/simulation/mowingTheField/mowing.in', 'r') as infile:
    n = int(infile.readline())
    data = []
    for _ in range(n):
        temp = infile.readline().split()
        data.append([temp[0], int(temp[1])])

cellVisits = [] # log visited cells and times
fjPosition = [0, 0]
for move in data: #move = ['N', 4]
    if move[0] == 'N':
        fjPosition[1] += move[1]
    if move[0] == 'E':
        fjPosition[0] += move[1]
    if move[0] == 'S':
        fjPosition[1] -= move[1]
    if move[0] == 'W':
        fjPosition[0] -= move[1]