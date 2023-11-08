with open('brokenBeads/beads.in', 'r') as infile:
    lines = infile.readlines()
    numBeads = (lines[0]).strip()
    necklace = lines[1]

necklace = [*necklace]

collectedList = []

for index in range(0, len(necklace)):
    bcolor = necklace[index-1]
    fcolor = necklace[index]

    # if color is white
    if bcolor == "w":
        bcolor = necklace[index-2]
    if fcolor == "w":
        fcolor = necklace[index+1]

    count = 0

    collectedBeads = 0

    substring1 = necklace[0:index] # string of broken necklacegoing backwards
    substring2 = necklace[index:len(necklace)] # string going fowards

    saves1 = substring1
    rev1 = substring1
    rev1.reverse()

    rev2 = substring2


    for x in rev2[::-1]:
        substring1.append(x)

    for x in necklace[0:index]:
        substring2.append(x)

    substring1.remove("\n")
    substring2.remove("\n")
    print(f"index: {index}, leftStr: {substring1}, rightStr: {substring2}")



    while (substring1[count] == bcolor) or (substring1[count] == "w"): # checking backwards
        collectedBeads += 1
        count += 1
        print(f"collected a {bcolor} bead")
    count = 0

    while (substring2[count] == fcolor) or (substring2[count] == "w"): # checking fwds
        collectedBeads += 1
        count += 1
        print(f"collected a {bcolor} bead")

    collectedList.append(collectedBeads)

    


with open('brokenBeads/beads.out', 'w') as outfile:
    outfile.write(str(max(collectedList) + 0))

print(collectedList)
print(max(collectedList) + 0)
