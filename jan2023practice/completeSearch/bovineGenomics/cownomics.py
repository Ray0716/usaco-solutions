def are_lists_disjoint(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    return len(set1.intersection(set2)) == 0    

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

spottyPositions = []
plainPositions = []

for index in range(m):
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
        spottyGenePositions += 1

with open('cownomics.out', 'w') as outfile:
    outfile.write(str(spottyGenePositions))