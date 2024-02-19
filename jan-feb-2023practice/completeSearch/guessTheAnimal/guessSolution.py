def intersection_of_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)

with open('guess.in', 'r') as infile:
    n = int(infile.readline())
    data = []
    for _ in range(n):
        temp = infile.readline().split()
        #temp.pop(1)
        data.append(temp)
numYes = []
for animal in data:
    for compareAnimal in data:
        if compareAnimal == animal:
            continue
        numYes.append(len(intersection_of_lists(animal[2:], compareAnimal[2:])) + 1)


#print(max(numYes))
#print(data)
with open('guess.out', 'w') as outfile:
    outfile.write(str(max(numYes)))