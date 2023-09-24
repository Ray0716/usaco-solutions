import sys

cowGrid = []

for line in sys.stdin.read():
    if " " not in line: # if first line
        n = int(line)
        continue
    else:
        cowGrid.append(line.split(' '))

    for cow in cowGrid:
        for coord in cow:
            coord = int(coord)


print(cowGrid)