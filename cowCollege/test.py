n = input()
data = input().split()
data = [int(x) for x in data]

data.sort()

tuitions = []
maxT = 0
p = 0
for index in range(len(data)):
    if (data[index] * (len(data) - index)) > maxT:
        maxT = (data[index] * (len(data) - index))
        p = data[index]

    
print(f"{maxT} {p}")




