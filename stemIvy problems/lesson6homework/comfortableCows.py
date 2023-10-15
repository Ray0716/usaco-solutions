import sys

cowGrid = []

    
def howManyComfyCow(otherCows): # returns the # of comfyCows in one instance of the pasture
    surroundingCows = 0
    comfyCows = 0

    for testingCow in otherCows:
        if [(testingCow[0]), (testingCow[1] + 1)] in otherCows:
            # print('adjacent cow found: ', [(testingCow[0]), (testingCow[1] + 1)], ' , testingcow: ', testingCow)
            surroundingCows += 1
        if [(testingCow[0]), (testingCow[1] - 1)] in otherCows:
            #print('adjacent cow found: ', [(testingCow[0]), (testingCow[1] - 1)], ' , testingcow: ', testingCow)
            surroundingCows += 1
        if [(testingCow[0] + 1), (testingCow[1])] in otherCows:
            #print('adjacent cow found: ', [(testingCow[0] + 1), (testingCow[1])], ' , testingcow: ', testingCow)
            surroundingCows += 1
        if [(testingCow[0] - 1), (testingCow[1])] in otherCows:
            #print('adjacent cow found: ', [(testingCow[0] - 1), (testingCow[1])], ' , testingcow: ', testingCow)
            surroundingCows += 1
        

        if surroundingCows == 3:
            comfyCows += 1
        surroundingCows = 0

    return comfyCows



n = input()

for x in range(int(n)):
    cowGrid.append((sys.stdin.readline()).split(' '))


for cow in cowGrid:
    for coord in cow:
        coord = int(coord)


cowGrid = [[int(coord.strip()) for coord in cow] for cow in cowGrid]
#print(cowGrid)

cowTestingGrid = []

comfyCows = 0
for cow in cowGrid:
    cowTestingGrid.append(cow)

    print(howManyComfyCow(cowTestingGrid))
