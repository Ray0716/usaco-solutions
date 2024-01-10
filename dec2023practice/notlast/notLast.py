with open('notlast.in', 'r') as inf:
    n = int(inf.readline())
    data = []
    for _ in range(n):
        temp = inf.readline().split()
        data.append([temp[0], int(temp[1])])


def sortl(smallerList): 
    smallerList.sort(key = lambda x: x[0],reverse=False) 
    return smallerList

cows = {
    "Bessie": 0,
    "Elsie": 0,
    "Daisy": 0,
    "Gertie": 0,
    "Annabelle": 0,
    "Maggie": 0,
    "Henrietta": 0
}

for milking in data:
    #print(f"c:{milking[0]}, muhc:{milking[1]}")
    cows[milking[0]] += milking[1]

milk = []
milk.append([cows["Bessie"], "Bessie"])
milk.append([cows["Elsie"], "Elsie"])
milk.append([cows["Daisy"], "Daisy"])
milk.append([cows["Gertie"], "Gertie"])
milk.append([cows["Annabelle"], "Annabelle"])
milk.append([cows["Maggie"], "Maggie"])
milk.append([cows["Henrietta"], "Henrietta"])

m = milk[0][0]
#print(milk , "   " , m)
milk = sortl(milk)

minimumMilkCow = min(cow[0] for cow in milk)

# Filter out the lists where the first element is equal to the minimum value
cowListWithMinimumRemoved = [cow for cow in milk if cow[0] > minimumMilkCow]




##milk = sortl(milk)
#print(milk)

#milk.remove(min(milk))
#print(cowListWithMinimumRemoved)


#print(min(milk))
with open('notlast.out', 'w') as outf:
    outf.write(str(min(cowListWithMinimumRemoved)[1]))

