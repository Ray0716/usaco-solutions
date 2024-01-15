def checkIfStopOrInfinte(cows, eatenSquares):
    for cowIndex in range(len(cows)):
        if [cows[cowIndex][1], cows[cowIndex][2]] in eatenSquares: # if current square has been eaten
            # if the next square for the cow is eaten already
            stopOrInfinite[cowIndex] = "s"
            data.remove(cows[cowIndex])
        if cows[cowIndex][0] == "N" and (not (any(cows[cowIndex][1] == cows[cowIndex][1] for sublist in cows) and any(cows[cowIndex][2] > cows[cowIndex][2] for cow in cows)))



n = int(input())
global data
data = []
for x in range(n):
    temp = input().split(" ")
    temp[1] = int(temp[1])
    temp[2] = int(temp[2])
    data.append(temp)


global stopOrInfinite
stopOrInfinite = [""] * len(data) # checks if each cow has stopped or weknow they go to infinity

eatenSquares = [] # the squares that are blank tha thave no grass
global squaresEaten
squaresEaten = [0] * len(data) # how many squares each cow eats

while any(len(s) <= 1 for s in my_list):
    # we don't know if 