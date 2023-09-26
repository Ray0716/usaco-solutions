farm = []

def divide(cows): # cows is list of one coordinates, returns the divide for the axis
    lessSide = 0
    greaterSide = 0
    differences = {}
    for testDivide in range(0, (max(cows)+1), 2):
        for cow in cows:
            if cow < testDivide:
                lessSide += 1
            if cow > testDivide:
                greaterSide += 1
        differences[testDivide] = abs(greaterSide - lessSide)
        lessSide = 0
        greaterSide = 0

    min_key = None
    min_value = float('inf')  # Initialize min_value with positive infinity

    print(differences)

    for key, value in differences.items():
        if value < min_value:
            min_key = key
            min_value = value

    return min_key

# we need to return the index of the divide that has the least difference
# (the key of the least value in the dict)




with open('/Users/Ray/Downloads/balancing_bronze_feb16/2.in', 'r') as infile:
    lines = infile.readlines()
    for line in lines:
        cow = line.split(' ')
        farm.append([int(cow[0]), int(cow[1])])

    del farm[0]

#print(farm)

xMid = {}
yMid = {}

xCoords = sorted([cow[0] for cow in farm])
yCoords = sorted([cow[1] for cow in farm])

#print(xCoords)
horizontalDiv = divide(xCoords) # the libne is vert
verticalDiv = divide(yCoords) # the line is horiz

print(horizontalDiv)
print(verticalDiv)

q1 = 0
q2 = 0
q3 = 0
q4 = 0

for cow in farm:
    if cow[0] > horizontalDiv: # if on right side
        if cow[1] > verticalDiv: # if on upper side of right
            q1 += 1
        if cow[1] < verticalDiv: # if on lower of right
            q4 += 1
    if cow[0] < horizontalDiv: # if on left side
        if cow[1] > verticalDiv: # if on upper side of left
            q2 += 1
        if cow[1] < verticalDiv: # if on lower of left
            q3 += 1


with open('/Users/Ray/compSci/usaco/lesson6homework/loadBalancing/balancing.out', 'w') as outfile:
    outfile.write(str(max(q1, q2, q3, q4)))


# dividing x coords (north-south fence)
