with open('pails.in', 'r') as infile:
    data = [int(x) for x in infile.readline().split()]

# print(data)

x = data[0]
y = data[1]
m = data[2]

numX = 0
mFillAmounts = []
while (numX * x) <= m:
    mFill = 0
    mFill += (numX * x)
    numY = 0
    while mFill + (numY * y) <= m:
        mFill += (numY * y)
        numY += 1

    mFillAmounts.append(mFill)

    numX += 1

with open('pails.out', 'w') as outfile:
    outfile.write(str(max(mFillAmounts)))