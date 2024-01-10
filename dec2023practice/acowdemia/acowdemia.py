nm = [int(x) for x in input().split()]
n = nm[0]
m = nm[1]
data = []
for x in range(n):
    data.append(list(input()))

friends = []
howManyFriend = 0
#print(data)

for row in range(len(data)):
    for col in range(len(data[row])):
        print(f"row:{row}, col:{col}")
        if data[row][col] == "G":
            # now we check if there are adjacent cows, if there are, we remove tem
            adjacentCows = 0
            #check bounds first, corners first, then edges
            if row == len(data) and col == len(data[row]): #lower right
                if data[row-1][col] == "C" and data[row][col-1] == "C":
                    adjacentCows += 2
            elif row == len(data) and col==0: #lower left
                if data[row-1][0] == "C" and data[row][1] == "C":
                    adjacentCows += 2
            elif row == 0 and col == len(data[row]): # upper right
                if data[0][col-1] == "C" and data[1][col] == "C":
                    adjacentCows += 2
            elif row == 0 and col == 0: #uper left
                if data[0][1] == "C" and data[1][0] == "C":
                    adjacentCows += 2



            elif row == 0: #top edge
                if data[row+1][col] == "C": #down
                    adjacentCows += 1
                #if data[row-1][col] == "C": #up
                if data[row][col+1] == "C": #right
                    adjacentCows += 1
                if data[row][col-1] == "C": #left
                    adjacentCows += 1
                    
            elif col == 0: #left edge
                if data[row+1][col] == "C": #down
                    adjacentCows += 1
                if data[row-1][col] == "C": #up
                    adjacentCows += 1
                if data[row][col+1] == "C": #right
                    adjacentCows += 1
                #if data[row][col-1] == "C": #left

            elif row == len(data): # bottom edge
                #if data[row+1][col] == "C": #down
                if data[row-1][col] == "C": #up
                    adjacentCows += 1
                if data[row][col+1] == "C": #right
                    adjacentCows += 1
                if data[row][col-1] == "C": #left
                    adjacentCows += 1

            elif col == len(data[row]): # right edge
                print("righterdf")
                if data[row+1][col] == "C": #down
                    adjacentCows += 1
                    print("cowfoound")
                if data[row-1][col] == "C": #up
                    adjacentCows += 1
                    print("cowfoound")

                #if data[row][col+1] == "C": #right
                if data[row][col-1] == "C": #left
                    adjacentCows += 1
                    print("cowfoound")



            else: #in the centeral region, check all 4 sides (up down left right) for cows
                #print("in central")
                if data[row+1][col] == "C": #down
                    adjacentCows += 1
                if data[row-1][col] == "C": #up
                    adjacentCows += 1
                if data[row][col+1] == "C": #right
                    adjacentCows += 1
                if data[row][col-1] == "C": #left
                    adjacentCows += 1

            print(adjacentCows)

            if adjacentCows >= 2: # there is a friend pair
                data[row][col] = "."
                # add cows to frind so we know what pair is already friends
                temp = []
                try:
                    if data[row+1][col] == "C": #down
                        temp.append([row+1, col])
                except:
                    pass
                try:
                    if data[row-1][col] == "C": #up
                        temp.append([row-1, col])
                except:
                    pass
                try:
                    if data[row][col+1] == "C": #right
                        temp.append([row, col+1])
                except:
                    pass
                try:
                    if data[row][col-1] == "C": #left
                        temp.append([row, col-1])
                except:
                    pass


                #print(temp)

                #if ([temp[0], temp[1]] not in friends) and ([temp[1], temp[0]] not in friends):
                friends.append(temp)
                howManyFriend += 1
                # we chec if duplicate cow pairs later, if there are we just decrement by one
            adjacentCows = 0


print(howManyFriend)
                



