nk = [int(x) for x in input().split()]
n = nk[0]
k = nk[1]

money = 0

def checkConsecutive(index, list):
    count = 0
    while list[index] == 1:
        index += 1
        count += 1
    return count

def nextOne(index, list):
    while index <= len(list) + 1 and list[index] != 1:
        index += 1
    if list[index] == 0:
        return 0
    else:
        return index

days = [int(x) for x in input().split()]
watchDays = [0 for x in range(max(days))]

for day in days:
    watchDays[day-1] = 1

#when you able to buy consecutive, buy consecutive when days are connected
# cvompare the days that are seperated by a gap

for day in range(len(watchDays)):
    if watchDays[day] == 1:
        dayNum = day + 1
        if day + 1 <= len(watchDays) - 1: #if we still in range
            cons = checkConsecutive(day, watchDays)
            if cons >= 1:
                money += (k + cons)
            else:
                dist = nextOne(day, watchDays) - day
                money += min((k + dist), (k+k+2))

print(money)

