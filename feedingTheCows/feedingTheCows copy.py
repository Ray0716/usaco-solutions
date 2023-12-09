t = input()
data = []

class testCase:
    def __init__(self, n, k , cows):
        self.n = n
        self.k = k
        self.cows = cows

caseList = []

def numGrass(list):
    count = 0
    for x in list:
        if x == "G" or x == "H":
            count += 1
    return count

def returnGrass(n, k, cows):
    if k == 0:
        return("".join(cows))

    grass = ["."] * len(cows)

    gi = 0 # vars for looping through and calculating where the G and H grasses are
    hi = 0

    # gi is iterating index through cow list
    # if the cow is a G then we make the gi+k space in the grasses a G grass
    # this because the range of the grass is
    # gi, gi+k, gi+2k
    # we assume the cow is at the leftmost of the range and then we place the grass at the middle
    # 

    
        

    while gi < n:
        if cows[gi] == "G":
            if gi + k < n: #checking if the target for the grass is out of range of the cowlist
                # in other words the middle of the range is not in fron tof a cow
                grass[gi + k] = "G" # make the middle of the range a grass
                gi += (gi + (2*k)) # skip ahead to end of the range
            else:
                grass[gi] = "G" #if out of range, make current cow is equal to the grass G
                gi += n
        else:
            gi += 1

    while hi < n:
        if cows[hi] == "H":
            if hi + k < n:
                if grass[hi+k] == ".": # no patch conflict with G
                    grass[hi + k] = "H"
                    hi += (hi + (2*k))
                else: #rthere is a patch conflict with g
                    grass[(hi+k) -1] = "H" # since we are moving left to right, we know that if we make the grass one less than the conflict position the cow will vbe in range of it
                    # note that the grass will either be 1 left or right of the conflic position
                    # in our case it will alwasy be 1 left
                    hi += (hi + (2*k))
            else:
                if grass[hi] == ".":
                    grass[hi] = "H"
                    hi += n
                else:
                    grass[hi-1] = "H"
                    hi += n
        else:
            hi += 1

    return "".join(grass)


for x in range(int(t) * 2):
    data.append(input())

for index in range(len(data)):
    if index % 2 == 0:
        caseList.append(testCase([int(y) for y in data[index].split()][0], [int(y) for y in data[index].split()][1], data[index + 1]))


for case in caseList:
    print(numGrass(returnGrass(case.n, case.k, case.cows)))
    print(returnGrass(case.n, case.k, case.cows))
