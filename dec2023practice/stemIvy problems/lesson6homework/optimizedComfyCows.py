import sys

def howManyComfyCow(x, y, occupied_cells):
    surroundingCows = 0
    coordinates = [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]

    for coord in coordinates:
        if coord in occupied_cells:
            surroundingCows += 1

    return surroundingCows == 3

n = int(input())
occupied_cells = set()
comfortable_cows_count = [0] * n

for i in range(n):
    x, y = map(int, input().split())
    occupied_cells.add((x, y))

    for coord in [(x, y), (x, y+1), (x, y-1), (x+1, y), (x-1, y)]:
        if coord in occupied_cells:
            comfortable_cows_count[i] += 1

    if i > 0:
        for j in range(i):
            cow_x, cow_y = map(int, input().split())
            if howManyComfyCow(cow_x, cow_y, occupied_cells):
                comfortable_cows_count[i] += 1

    print(comfortable_cows_count[i])
