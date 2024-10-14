nq = [int(x) for x in input().split()]
n = nq[0]
q = nq[1]

closingTimes = [int(x) for x in input().split()]
visitTimes = [int(x) for x in input().split()]
queries = []

for _ in range(q):
    queries.append([int(x) for x in input().split()])

for q in queries:
    v = q[0]
    s = q[1]
    farmsCanVisit = 0
    for farmIndex in range(n):
        if s + visitTimes[farmIndex] < closingTimes[farmIndex]:
            farmsCanVisit += 1
        else:
            continue
    if farmsCanVisit >= v:
        print("YES")
    else:
        print("NO")