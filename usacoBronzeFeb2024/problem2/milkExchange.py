nm = [int(x) for x in input().split()]
n = nm[0]
m = nm[1]

cowExchange = [*input()]

cowBuckets = [int(x) for x in input().split()]
capacities = cowBuckets.copy()

spilled = 0

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
        if cowBuckets[cowIndex] >= m:
            cowBuckets[cowIndex] -= m
            cowBuckets[rightCow] += m
            
    if dir == 'L':
        if cowBuckets[cowIndex] >= m:
            cowBuckets[cowIndex] -= m
            cowBuckets[leftCow] += m
                
for index in range(n):
    if cowBuckets[index] > capacities[index]:
        spilled += cowBuckets[index] - capacities[index]


print(sum(cowBuckets) - spilled)
                    


