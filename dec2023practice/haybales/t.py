def addOnes(d, n, list): # go thru list, scatter points of 1's throuh list for exaple 4, 3 is 1, 1, 1 starting from index 4
    num = n
    d = d-1
    for x in range(len(list)):
        if x >= d and num != 0:
            list[x] = 1
            num -= 1


def a(d, n, list): # go thru list, scatter points of 1's throuh list for exaple 4, 3 is 1, 1, 1 starting from index 4
    d = d-1
    if d == len(list)-1:
        list[-1] = 1
    elif n < len(list):
        list[d:d+n] = [1 for _ in range(len(list[d:d+n]))]
    elif n >= len(list):
        list[d:-1] = [1 for _ in range(len(list[d:-1]))]
    

m = [0, 0, 0, 0, 0]

a(1, 2, m)

print(m)

a(5, 10, m)

print(m)