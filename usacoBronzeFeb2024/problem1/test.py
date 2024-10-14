t = int(input())
result = []
for _ in range(t):
    numberOfStones = input()
    ch = numberOfStones[-1]
    if ch == '0':
        result.append("E")
    else:
        result.append("B")

for x in result:
    print(x)

