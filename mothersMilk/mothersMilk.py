with open('mothersMilk/milk3.in', 'r') as infile:
    line = infile.readline()
    bucketCapacities = line.split(" ")
    bucketCapacities = [int(x) for x in bucketCapacities]

maxA = bucketCapacities[0]
maxB = bucketCapacities[1]
maxC = bucketCapacities[2]

print(f"a: {maxA}, b:{maxB}, c:{maxC}")

global states
states = []

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
        states.append(state(a, b, c))
    elif b == 0 and fromBucket == "b":
        states.append(state(a, b, c))
    elif c == 0 and fromBucket == "c":
        states.append(state(a, b, c))
    elif fromBucket == "a" and toBucket == "b":
        if state(0, (a+b), c) or state(((a+b)-maxB), maxB, c) in states:
            pass
        elif (a+b) <= maxB:
            states.append(state(0, (a+b), c))
            print("appended somethign to states")
        else:
            states.append(state(((a+b)-maxB), maxB, c))
            print("appended somethign to states")
    elif fromBucket == "a" and toBucket == "c":
        if state(0, b, (a+c)) or state(((a+c)-maxC), b, maxC) in states:
            pass
        elif (a+c) <= maxC:
            states.append(state(0, b, (a+c)))
            print("appended somethign to states")
        else:
            states.append(state(((a+c)-maxC), b, maxC))
            print("appended somethign to states")

    elif fromBucket == "b" and toBucket == "a":
        if state((a+b), 0, c) or state(maxA, ((a+b)-maxB), c) in states:
            pass
        elif (a+b) <= maxA:
            states.append(state((a+b), 0, c))
            print("appended somethign to states")
        else:
            states.append(state(maxA, ((a+b)-maxB), c))
            print("appended somethign to states")
    elif fromBucket == "b" and toBucket == "c":
        if state(a, 0, (b+c)) or state(a, ((b+c)-maxC), maxC) in states:
            pass
        elif (b+c) <= maxC:
            states.append(state(a, 0, (b+c)))
            print("appended somethign to states")
        else:
            states.append(state(a, ((b+c)-maxC), maxC))
            print("appended somethign to states")

    elif fromBucket == "c" and toBucket == "a":
        if state((a+c), b, 0) or state(maxA, b, ((a+c)-maxC)) in states:
            pass
        elif (a+c) <= maxA:
            states.append(state((a+c), b, 0))
            print("appended somethign to states")
        else:
            states.append(state(maxA, b, ((a+c)-maxC)))
            print("appended somethign to states")
    elif fromBucket == "c" and toBucket == "b":
        if state(a, (b+c), 0) or state(a, maxB, ((b+c)-maxB)) in states:
            pass
        elif (b+c) <= maxB:
            states.append(state(a, (b+c), 0))
            print("appended somethign to states")
        else:
            states.append(state(a, maxB, ((b+c)-maxB)))
            print("appended somethign to states")

buckets = ["a", "b", "c"]

for a in range(maxA):
    for b in range(maxB):
        for c in range(maxC):
            if (a+b+c) == maxC:
                for f in range(0, 3):
                    for t in range(0, 3):
                        if f != t:
                            edge(a, b, c, str(buckets[f]), str(buckets[t]))
                            print(f"{a}, {b}, {c}, {buckets[f]}, {buckets[t]}")


print(states)