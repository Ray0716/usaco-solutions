nk = [int(x) for x in input().split()]
n = nk[0]
k = nk[1]

money = 0


days = [int(x) for x in input().split()]


for dayIndex in range(n):
    if dayIndex == 0:
        money += k + 1
    else:
        money += min((k+1), ((days[dayIndex] - days[dayIndex -1]) + 0))

print(money)

