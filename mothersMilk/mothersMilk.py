with open('mothersMilk/milk3.in', 'r') as infile:
    line = infile.readline()
    bucketCapacities = line.split(" ")
    bucketCapacities = [int(x) for x in bucketCapacities]

maxA = bucketCapacities[0]
maxB = bucketCapacities[1]
maxC = bucketCapacities[2]

 
global states
states = []

global access
access = [[[0 for _ in range(maxC+1)] for _ in range(maxB+1)] for _ in range(maxA+1)]


class state: # single state of a bucket config (ex, 0 0 10)
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

def edge(a, b, c, fromBucket, toBucket):
    ''' edge func moves through states tree with BFS, 
    adds states to the list
    in the end we will check list because it have all the states 
    we loop through all different permutations of from and to buckets later,
    and plug them into this function '''
    # from  and to bucket is string ab or c
    # abc are ints
    if a == 0 and fromBucket == "a":
        return
        #states.append(state(a, b, c))
    elif b == 0 and fromBucket == "b":
        return
        #states.append(state(a, b, c))
    elif c == 0 and fromBucket == "c":
        return
        #states.append(state(a, b, c))


    elif fromBucket == "a" and toBucket == "b":
        if a+b <= maxB:
            if access[0][a+b][c] != 1:
                states.append(state(0, a+b, c))
                access[0][a+b][c] = 1
        else:
            if access[(a+b)-maxB][maxB][c] != 1:
                states.append(state(((a+b)-maxB), maxB, c))
                access[(a+b)-maxB][maxB][c] = 1

    

    elif fromBucket == "a" and toBucket == "c":
        if a+c <= maxC:
            if access[0][b][a+c] != 1:
                states.append(state(0, b, a+c))
                access[0][b][a+c] = 1
        else:
            if access[(a+c)-maxC][b][maxC] != 1:
                states.append(state(((a+c)-maxC), b, maxC))
                access[(a+c)-maxC][b][maxC] = 1



    elif fromBucket == "b" and toBucket == "a":
        if b+a <= maxB:
            try:
                if access[a+b][0][c] != 1:
                    states.append(state(a+b, 0, c))
                    access[a+b][0][c] = 1
            except:
                pass
        else:
            if access[maxA][(a+b)-maxA][c] != 1:
                states.append(state(maxA, ((a+b)-maxA), c))
                access[maxA][(a+b)-maxA][c] = 1



    elif fromBucket == "b" and toBucket == "c":
        if b+c <= maxC:
            if access[a][0][b+c] != 1:
                states.append(state(a, 0, b+c))
                access[a][0][b+c] = 1
        else:
            if access[a][(b+c)-maxC][maxC] != 1:
                states.append(state(a, ((b+c)-maxC), maxC))
                access[a][(b+c)-maxC][maxC] = 1



    elif fromBucket == "c" and toBucket == "a":
        if c+a <= maxA:
            if access[c+a][b][0] != 1:
                states.append(state((c+a), b, 0))
                access[c+a][b][0] = 1
        else:
            if access[maxA][b][(a+c)-maxA] != 1:
                states.append(state(maxA, b, (a+c)-maxA))
                access[maxA][b][(a+c)-maxA] = 1



    elif fromBucket == "c" and toBucket == "b":
        if c+b <= maxB:
            if access[a][b+c][0] != 1:
                states.append(state(a, (b+c), 0))
                access[a][b+c][0] = 1
        else:
            if access[a][maxB][(b+c)-maxB] != 1:
                states.append(state(a, maxB, (b+c)-maxB))
                access[a][maxB][(b+c)-maxB] = 1

buckets = ["a", "b", "c"]

#print(len(access))

states.append(state(0, 0, maxC))

while len(states) != 0:
    node = states[0]
    states.remove(states[0])

    for f in range(0,3):
        for t in range(0,3):
            if f != t:
                edge(node.a, node.b, node.c, buckets[f], buckets[t])
                #print(f"a: {node.a}, b:{node.b}, c:{node.c}, f:{buckets[f]}, t:{buckets[t]}")


results = []

for i in range(0,maxB+1):
    for j in range(0,maxC+1):
        if access[0][i][j] == 1:
            results.append(j)

results.sort()

print(results)
    




'''
for c in range(20**3):
    for x in states:
        for f in range(0, 3):
            for t in range(0, 3):
                if f != t:
                    edge(x.a, x.b, x.c, str(buckets[f]), str(buckets[t]))
                    print(f"{x.a}, {x.b}, {x.c}, {buckets[f]}, {buckets[t]}")

'''

'''
for a in range(maxA+1):
    for b in range(maxB+1):
        for c in range(maxC+1):
            if (a+b+c) == maxC:
                for f in range(0, 3):
                    for t in range(0, 3):
                        if f != t:
                            edge(a, b, c, str(buckets[f]), str(buckets[t]))
                            print(f"{a}, {b}, {c}, {buckets[f]}, {buckets[t]}")


'''
'''
edge(8, 0, 2, "a", "c")

print(states)
print(states[0].a)
print(states[0].b)
print(states[0].c)

'''
