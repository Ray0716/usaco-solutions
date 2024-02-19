with open('jan2023practice/completeSearch/guessTheAnimal/guess.in', 'r') as infile:
    n = int(infile.readline())
    data = []
    for _ in range(n):
        temp = infile.readline().split()
        #temp.pop(1)
        data.append(temp)
numYes = []
for animal in data:
    print(animal, "---")
    nonUniqueAttributes = 0
    for attribute in animal[2:]:
        foundNonUnique = False
        for compareAnimal in data:
            if foundNonUnique:
                break
            if compareAnimal == animal:
                continue
            if attribute in compareAnimal[2:]:
                if foundNonUnique is False:
                    nonUniqueAttributes += 1
                    foundNonUnique = True
                    print("found nonunique attr ", attribute)


    if nonUniqueAttributes < int(animal[1]):
        numYes.append(nonUniqueAttributes + 1)
    else:
        numYes.append(nonUniqueAttributes)
#print(max(numYes))
#print(data)
with open('jan2023practice/completeSearch/guessTheAnimal/guess.out', 'w') as outfile:
    outfile.write(str(max(numYes)))