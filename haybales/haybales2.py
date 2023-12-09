nt = input().split()
n = int(nt[0])
t = int(nt[1])

data = []
for x in range(n):
    data.append([int(x) for x in input().split()])
data.append([t+1, 0])

remainingHay = 0
totalDelivered = 0
lastDeliveryDay = 0
for x in range(len(data)):
    totalDelivered += data[x][1]
    remainingHay -= data[x][0] - lastDeliveryDay # calculate how much hay was eaten / remain after gap in time
    lastDeliveryDay = data[x][0]
    remainingHay = max(remainingHay, 0) + data[x][1]

print(totalDelivered - remainingHay)

