'''
input:
N, T (N lines after, T is amximum days)
bi, di (n lines of this, bi is num bales di is day delivered)

1. make function to iterate over portion of list
    if the day has hay make it a 1
    if not 0
2. loop thru this list from start to T
    if list[x] = 1, hayeaten += 1

output

'''
balesEaten = 0

def addOnes(d, n, list): # go thru list, scatter points of 1's throuh list for exaple 4, 3 is 1, 1, 1 starting from index 4
    d = d-1
    if d == len(list)-1:
        list[-1] = 1
    elif n < len(list):
        list[d:d+n] = [1 for _ in range(len(list[d:d+n]))]
    elif n >= len(list):
        list[d:-1] = [1 for _ in range(len(list[d:-1]))]


nt = input().split()
n = int(nt[0])
t = int(nt[1])

data = []
for x in range(n):
    data.append([int(x) for x in input().split()])

baleList = [0 for x in range(t)]

for x in data:
    addOnes(x[0], x[1], baleList)

print(sum(baleList))
