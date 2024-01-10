with open('square.in', 'r') as infile:
    line1 = infile.readline()
    line2 = infile.readline()
    x1, y1, x2, y2 = line1.split(" ")
    x3, y3, x4, y4 = line2.split(" ")
    x1, x2, x3, x4, y1, y2, y3, y4 = int(x1), int(x2), int(x3), int(x4), int(y1), int(y2), int(y3), int(y4)
    print(x1, y1, x2, y2)
    print(x3, y3, x4, y4)

    ulim = max(y1, y2, y3, y4)
    dlim = min(y1, y2, y3, y4)
    rlim = max(x1, x2, x3, x4)
    llim = min(x1, x2, x3, x4)

    print(ulim, dlim, rlim, llim)

with open('square.out', 'w') as outfile:
    outfile.write(str((max((rlim-llim),(ulim-dlim)))**2))
