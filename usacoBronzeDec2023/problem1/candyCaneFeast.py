nm = [int(x) for x in input().split()]
n = nm[0]
m = nm[1]

cowHeights = [int(y) for y in input().split()]
candyCaneHeights = [int(z) for z in input().split()]

for candyCane in range(len(candyCaneHeights)):
    heightOffGround = 0
    for cow in range(len(cowHeights)):
        print(f"cow, caNDYCANE: {cowHeights[cow]}, {candyCaneHeights[candyCane]}")
        print(f"candyhgith:{candyCaneHeights}")
        if cowHeights[cow] >= (candyCaneHeights[candyCane] + heightOffGround): #can eat all of the  height
            cowHeights[cow] += candyCaneHeights[candyCane]
            candyCaneHeights[candyCane] = 0
        elif cowHeights[cow] <= heightOffGround: #cow cannot reach
            pass
        elif cowHeights[cow] > heightOffGround:
            heightOffGround = cowHeights[cow]
            cowHeights[cow] = cowHeights[cow] + (cowHeights[cow] - heightOffGround)
            candyCaneHeights[candyCane] -= cowHeights[cow]

print(cowHeights)

