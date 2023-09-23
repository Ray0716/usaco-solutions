levelsBefore = list()
levelsAfter = list()

with open('promote.in', 'r') as inFile:
    for lines in inFile:
        before, after = tuple(lines.split(' '))
        before, after = int(before), int(after)
        levelsBefore.append(before)
        levelsAfter.append(after)    