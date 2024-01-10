def pour(cap1, am1, cap2, am2):
    if am1 > (cap2 - am2):
        return [int(am1 - (cap2 - am2)), cap2]
    elif am1 == (cap2 - am2):
        return [0, cap2]
        print("OK")
    else:
        return [0, int(am1 + am2)]
        print("OK")


n = int(input())
b = []

for x in range(3):
    b.append([int(x) for x in input().split()])

    

# bucket [capacity, amount]
final = b.copy()
buckets = b.copy()
for x in range(len(buckets)-1):
    p = pour(buckets[x][0], buckets[x][1], buckets[x+1][0], buckets[x+1][1])
    final[x][1] = p[0]
    final[x+1][1] = p[1]
    print("b: ", buckets)
    print(f"c1:{buckets[x][0]}, a1:{buckets[x][1]}, c2:{buckets[x+1][0]}, a2:{buckets[x+1][1]}")
    print(pour(buckets[x][0], buckets[x][1], buckets[x+1][0], buckets[x+1][1]))

#final[-1][1] = pour(buckets[-2][0], buckets[-2][1], buckets[-1][0], buckets[-1][1])[1]

#final[-1][1] = int(buckets[-2][1] + final[-1][1])
print(final)


