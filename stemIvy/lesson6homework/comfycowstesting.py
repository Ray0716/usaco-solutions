def howManyComfyCow(otherCows): # returns the # of comfyCows in one instance of the pasture
    surroundingCows = 0
    comfyCows = 0

    for testingCow in otherCows:
        if [(testingCow[0]), (testingCow[1] + 1)] in otherCows:
            print('adjacent cow found: ', [(testingCow[0]), (testingCow[1] + 1)], ' , testingcow: ', testingCow)
            surroundingCows += 1
        if [(testingCow[0]), (testingCow[1] - 1)] in otherCows:
            print('adjacent cow found: ', [(testingCow[0]), (testingCow[1] - 1)], ' , testingcow: ', testingCow)
            surroundingCows += 1
        if [(testingCow[0] + 1), (testingCow[1])] in otherCows:
            print('adjacent cow found: ', [(testingCow[0] + 1), (testingCow[1])], ' , testingcow: ', testingCow)
            surroundingCows += 1
        if [(testingCow[0] - 1), (testingCow[1])] in otherCows:
            print('adjacent cow found: ', [(testingCow[0] - 1), (testingCow[1])], ' , testingcow: ', testingCow)
            surroundingCows += 1
        

        if surroundingCows == 3:
            comfyCows += 1
        surroundingCows = 0

    return comfyCows


cowGrid = [[0,1],[1,0],[1,1],[1,2]]

print(howManyComfyCow(cowGrid))