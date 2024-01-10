nm = [int(x) for x in input().split()]
n = nm[0]
m = nm[1]

cows = [int(y) for y in input().split()]
candys = [int(z) for z in input().split()]

for cane in range(m):
    heightOffGround = 0
    for cow in range(n):
        if cows[cow] <= heightOffGround: #not able to reach
            continue
        elif cows[cow] >= (candys[cane] + heightOffGround):
            cows[cow] += candys[cane]
            candys[cane] = 0
        elif cows[cow] > heightOffGround and cows[cow] < (candys[cane] + heightOffGround):
            eaten = (cows[cow] - heightOffGround)
            cows[cow] += eaten
            heightOffGround += eaten
            candys[cane] -= eaten
        

for cow in cows:
    print(cow)

        


