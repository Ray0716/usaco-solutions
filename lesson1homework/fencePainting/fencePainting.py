paintNs = []
allnums = [4, 5, 6, 3]
with open('paint.in', 'r') as inFile:
    line1 = inFile.readline()
    x1, x2 = line1.split(" ")
    x1, x2 = int(x1), int(x2)
    line2 = inFile.readline()
    x3, x4 = line2.split(" ")
    x3, x4 = int(x3), int(x4)
    
    allnums = [x1, x2, x3, x4]



        
        

with open('paint.out', 'w') as outFile:
    if x3 <= x2:
        if x1 > x4:
            outFile.write(str((x2-x1) + (x4-x3)))
        else:
            outFile.write(str(max(allnums) - min(allnums)))

    elif (x1 + x2 + x3 + x4) == 0:
        outFile.write(0)

    else:
        outFile.write(str((x2-x1) + (x4-x3)))

