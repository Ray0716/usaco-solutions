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

def findHaybalesEaten(d, b, t):
    if t-d == 0 and b != 0:
        return 1
    elif b > t-d:
        return t-d
    elif b <= t-d:
        return b


nt = input().split()
n = int(nt[0])
t = int(nt[1])

data = []
for x in range(n):
    data.append([int(x) for x in input().split()])

for hayDelivery in data:
    balesEaten += findHaybalesEaten(hayDelivery[0], hayDelivery[1], t)

print(balesEaten)



