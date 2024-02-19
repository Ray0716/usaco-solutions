def common_elements(list1, list2):
    for sublist in list1:
        if sublist in list2:
            return True
    return False

with open('cownomics.in', 'r') as infile:
    nm = [int(x) for x in infile.readline().split()]
    n = nm[0]
    m = nm[1]
    spotty = []
    plain = []
    for _ in range(n):
        spotty.append([x for x in infile.readline() if x != "\n"])
    for _ in range(n):
        plain.append([x for x in infile.readline() if x != "\n"])

#print(spotty, plain)

spottyPositions = []
plainPositions = []



for pos1 in range(m):
    for pos2 in range(pos1, m):
        if pos2 == pos1:
            continue
        for pos3 in range(pos2, m):
            if pos3 == pos1 or pos3 == pos2:
                continue
            temp = []
            for cow in spotty:
                temp.append([cow[pos1], cow[pos2], cow[pos3]])
            spottyPositions.append(temp)

for pos1 in range(m):
    for pos2 in range(pos1, m):
        if pos2 == pos1:
            continue
        for pos3 in range(pos2, m):
            if pos3 == pos1 or pos3 == pos2:
                continue
            temp = []
            for cow in plain:
                temp.append([cow[pos1], cow[pos2], cow[pos3]])
            plainPositions.append(temp)

positions = 0
for index in range(len(spottyPositions)):
    if not common_elements(spottyPositions[index], plainPositions[index]):
        positions += 1
            
                





'''for index in range(m):
    thisPosition = []
    for cowGenome in spotty:
        thisPosition.append(cowGenome[index])
    spottyPositions.append(thisPosition)
    
for index in range(m):
    thisPosition = []
    for cowGenome in plain:
        thisPosition.append(cowGenome[index])
    plainPositions.append(thisPosition)
    
spottyGenePositions = 0

for index in range(len(spottyPositions)):
    if are_lists_disjoint(spottyPositions[index], plainPositions[index]):
        spottyGenePositions += 1'''

with open('cownomics.out', 'w') as outfile:
    outfile.write(str(positions))
