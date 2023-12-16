def flip(array, row, col):
    for r in range(len(array)):
        for c in range(len(array[r])):
            if r <= row and c <= col:
                if array[r][c] == 0:
                    array[r][c] = 1
                else:
                    array[r][c] = 0

    return array

with open('cowtip/cowtip.in', 'r') as inFile:
    n = int(inFile.readline())
    data = []
    for x in range(n):
        data.append(inFile.readline().split())
        data[x] = [int(g) for g in data[x][0]]

flips = 0
#print(data)

for row in range(len(data)-1, -1, -1):
    for col in range(len(data[row])-1, -1, -1):
        #print(f"r:{row}, c:{col}")
        if data[row][col] == 1:
            data = flip(data, row, col)
            #print(data)
            
            flips += 1

#print(flips)


with open('cowtip.out', 'w') as outFile:
    