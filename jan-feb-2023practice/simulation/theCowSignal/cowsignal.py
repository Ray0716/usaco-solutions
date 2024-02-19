def multiplyLine(l, n):
    res = []
    for e in l:
        for _ in range(n):
            res.append(e)

    return res

with open('cowsignal.in', 'r') as infile:
    mnk = [int(x) for x in infile.readline().split()]
    m = mnk[0]
    k = mnk[2]
    data = []
    for x in range(m):
        l = [*infile.readline().strip()]
        data.append(l)

resultList = []
    
for line in data:
    for _ in range(k):
        resultList.append(multiplyLine(line, k))

with open('cowsignal.out', 'w') as outfile:
    for line in resultList:
        outfile.write("".join(line))
        outfile.write("\n")