nm = [int(x) for x in input().split()]
n = nm[0]
m = nm[1]

cowExchange = [*input()]

cowBuckets = [int(x) for x in input().split()]
capacities = cowBuckets.copy()

spilled = 0

for minute in range(m):
    #pour process
    for cowIndex in range(n):
        if cowIndex == 0:
            leftCow = n-1
            rightCow = 1
        elif cowIndex == n-1:
            leftCow = n-2
            rightCow = 0
        else:
            leftCow = cowIndex - 1
            rightCow = cowIndex + 1
        dir = cowExchange[cowIndex]

        if dir == 'R':
            if cowBuckets[cowIndex] >= 1:
                cowBuckets[cowIndex] -= 1
                cowBuckets[rightCow] += 1
                
        if dir == 'L':
            if cowBuckets[cowIndex] >= 1:
                cowBuckets[cowIndex] -= 1
                cowBuckets[leftCow] += 1
                
for index in range(n):
    if cowBuckets[index] > capacities[index]:
        spilled += cowBuckets[index] - capacities[index]


print(sum(cowBuckets) - spilled)
                    


