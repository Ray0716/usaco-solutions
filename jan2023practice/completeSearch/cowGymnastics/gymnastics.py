def elements_after(lst, element):
    try:
        index = lst.index(element)
        result = lst[index + 1:]
        result.sort()
        return result
    except ValueError:
        return []


def lists_intersection(lists):
    if not lists:
        return []

    # Convert each list to a set
    sets = [set(lst) for lst in lists]

    # Find the intersection using the first set as a starting point
    intersection = sets[0].intersection(*sets[1:])

    return list(intersection)



with open('gymnastics.in', 'r') as infile:
    kn = [int(x) for x in infile.readline().split()]
    k = kn[0]
    n = kn[1]
    data = []
    for _ in range(k):
        data.append([int(x) for x in infile.readline().split()])
    
numCows =  max(data[0])

pairs = 0

for cow in range(1, numCows + 1):
    worseCows = []
    cowsThatDidWorseThanThisCow = []
    for performance in data:
        cowsThatDidWorseThanThisCow.append(elements_after(performance, cow))
    worseCows = lists_intersection(cowsThatDidWorseThanThisCow)
    pairs += len(worseCows)
    worseCows = []


with open('gymnastics.out','w') as outfile:
    outfile.writelines(str(pairs))
    