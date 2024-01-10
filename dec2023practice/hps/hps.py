with open('hps.in', 'r') as inFile:
    n = int(inFile.readline())
    data = []
    for _ in range(n):
        data.append([int(x) for x in inFile.readline().split()])

gamesWon = [0, 0, 0, 0, 0, 0]
abc = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
a = 1
b = 2
c = 3
# a->b, b->c, c->a
#print(f"a:{a}, b:{b}, c:{c}")

for x in range(6):
    for game in data:
        if game[0] == a and game[1] == b:
            gamesWon[x] += 1
        if game[0] == b and game[1] == c:
            gamesWon[x] += 1
        if game[0] == c and game[1] == a:
            gamesWon[x] += 1

    a = abc[x][0]
    b = abc[x][1]
    c = abc[x][2]
    ##print(f"a:{a}, b:{b}, c:{c}")
    #print(gamesWon)




#print(max(gamesWon))


with open('hps.out', 'w') as outf:
    outf.write(str(max(gamesWon)))