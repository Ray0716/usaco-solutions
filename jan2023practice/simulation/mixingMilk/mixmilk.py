def pour(bucket1, bucket2):
    b1c = bucket1[0]
    b1a = bucket1[1]
    b2c = bucket2[0]
    b2a = bucket2[1]

    # b1 -> b2

    if b2a + b1a > b2c: # ovbervlw
        return [(b2a + b1a) - b2c, b2c]
    elif b2a + b1a == b2c:
        return [0, b2c]
    else:
        return [0, b2a+b1a]

with open("mixmilk.in", "r") as infile:
    data = []
    for x in range(3):
        data.append([int(x) for x in infile.readline().split()])

i1 = 0
i2 = 1
i3 = 2

for x in range(32):
    i1 -= 1
    i2 -= 1
    i3 -= 1
    i1 = i1 % 3
    i2 = i2 % 3
    i3 = i3 % 3
    
    abPour = pour(data[i1], data[i2])
    data[i1][1] = abPour[0]
    data[i2][1] = abPour[1]

    bcPour = pour(data[i2], data[i3])
    data[i2][1] = bcPour[0]
    data[i3][1] = bcPour[1]

    caPour = pour(data[i3], data[i1])
    data[i3][1] = caPour[0]
    data[i1][1] = caPour[1]

    #print(data[0][1], data[1][1], data[2][1], x)


with open("mixmilk.out", "w") as outfile:
    outfile.write(str(data[0][1]))
    outfile.write("\n")
    outfile.write(str(data[1][1]))
    outfile.write("\n")
    outfile.write(str(data[2][1]))
