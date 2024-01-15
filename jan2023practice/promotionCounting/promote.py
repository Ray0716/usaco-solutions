with open('promote.in', 'r') as infile:
    data = []
    for _ in range(4):
        data.append([int(x) for x in [x.strip("\n") for x in infile.readline().split(" ")]])


bronzeToSilver = 0
silverToGold = 0
goldToPlat = 0

BB = data[0][0]
BA = data[0][1]
SB = data[1][0]
SA = data[1][1]
GB = data[2][0]
GA = data[2][1]
PB = data[3][0]
PA = data[3][1]


goldToPlat = PA - PB
silverToGold = GA - GB + PA - PB
bronzeToSilver = SA - SB + GA - GB + PA - PB # TODO analyze this tmrw 1.13.24

with open('promote.out', 'w') as outFile:
    outFile.write(str(bronzeToSilver))
    outFile.write("\n")
    outFile.write(str(silverToGold))
    outFile.write("\n")
    outFile.write(str(goldToPlat))