"""
ID: raytang
LANG: PYTHON3
TASK: beads
"""
infname = "beads.in"
outfname = "beads.out"

def isAllEqual(list):
    return all(i == list[0] for i in list)

with open(infname, 'r') as infile:
    lines = infile.readlines()
    numBeads = (lines[0]).strip()
    necklace = lines[1]

if isAllEqual(necklace) == True:
    with open(outfname, 'w') as outfile:
        outfile.write(str(len(necklace) + 0))
        outfile.write("\n")
    exit()


necklace = [*necklace]

collectedList = []



for index in range(0, len(necklace)):
    bcolor = necklace[index-1]
    fcolor = necklace[index]

    # if color is white
    whiteCountBack = 0
    whiteCountFwd = 0
    while bcolor == "w":
        bcolor = necklace[index-(whiteCountBack + 2)]
        whiteCountBack += 1
    while fcolor == "w":
        fcolor = necklace[index+(whiteCountFwd + 1)]
        whiteCountFwd += 1

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

    for y in necklace[0:index]:
        substring2.append(y)
    


    try:
        substring1.remove("\n")
        substring2.remove("\n")
    except:
        pass
    #print(f"index: {index}, leftStr: {substring1}, rightStr: {substring2}")


    try:
        while (substring1[count] == bcolor) or (substring1[count] == "w"): # checking backwards
            collectedBeads += 1
            count += 1
            #print(f"collected a {bcolor} bead")
        count = 0
    except:
        pass

    try:
        while (substring2[count] == fcolor) or (substring2[count] == "w"): # checking fwds
            collectedBeads += 1
            count += 1
            #print(f"collected a {bcolor} bead")
        count = 0
    except:
        pass

    collectedList.append(collectedBeads)

if collectedList == []:
    collectedList.append(0)

if isAllEqual(necklace) == False:  
    with open(outfname, 'w') as outfile:
        outfile.write(str(max(collectedList) + 0))
        outfile.write("\n")

#print(max(collectedList) + 0)
