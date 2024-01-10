n = input()
data = input().split()
data = [int(x) for x in data]

avg = round(sum(data) / len(data))
money = 0


for cow in data:
    if cow >= avg:
        money += avg

print(f"{money} {avg}")

