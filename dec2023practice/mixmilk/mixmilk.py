def pour(cap1, am1, cap2, am2):
    if am1 > (cap2 - am2):
        return [int(am1 - (cap2 - am2)), cap2]
    elif am1 == (cap2 - am2):
        return [0, cap2]
        print("OK")
    else:
        return [0, int(am1 + am2)]
        print("OK")


def pourHundred(bucketList):
    for x in range(100):
        p = pour(bucketList[x%3][0], bucketList[x%3][1], bucketList[(x%3)+1][0], bucketList[(x%3)+1][1])
        bucketList[x%3] = p[0]
        bucketList[(x%3) + 1] = p[1]
    return bucketList



b = []

with open('mixmilk/mixmilk.in', 'r') as inFile:
    for x in range(3):
        b.append([int(x) for x in inFile.readline().split()])

print(b)

with open('mixmilk/mixmilk.out', 'w') as outFile:
    outFile.write(pourHundred(b))

# bucket [capacity, amount]
#ets[-2][0], buckets[-2][1], buckets[-1][0], buckets[-1][1])[1]

#final[-1][1] = int(buckets[-2][1] + final[-1][1])



