nq = [int(x) for x in input().split()]
n = nq[0]
q = nq[1]



closingTimes = [int(x) for x in input().split()]
visitTimes = [int(x) for x in input().split()]
queries = []
#difference = [x - y for x, y in zip(closingTimes, visitTimes)]

for _ in range(q):
    queries.append([int(x) for x in input().split()])

for q in queries:
    v = q[0]
    s = q[1]
    farmsCanVisit = 0
    test = [x+s for x in visitTimes]
    for i in range(n):
        if test[i] < closingTimes[i]:
            farmsCanVisit += 1
    if farmsCanVisit >= v:
        print("YES")
    else:
        print("NO")