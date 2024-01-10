n = int(input())
blocks = []
for x in range(4):
    blocks.append([*input()])

words = []
for y in range(n):
    words.append([*input()])
#print(words)



for word in words:
    canSpell = False
    if len(word) == 4:
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    for d in range(4):
                        if a != b and a != c and a != d and b != c and b != d and c != d:
                            #print(f"{a}, {b}, {c}, {d}")
                            if word[0] in blocks[a]:
                                if word[1] in blocks[b]:
                                    if word[2] in blocks[c]:
                                        if word[3] in blocks[d]:
                                            canSpell = True

        if not canSpell:
            print("NO")
        else:
            print("YES")
            canSpell = False

    if len(word) == 3:
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    for d in range(4):
                        if a != b and a != c and a != d and b != c and b != d and c != d:
                            #print(f"{a}, {b}, {c}, {d}")
                            if word[0] in blocks[a] and word[1] in blocks[b] and word[2] in blocks[c]:
                                #print(f"1let:{word[0]}, blok:{blocks[a]}")
                                #print(f"2let:{word[1]}, blok:{blocks[b]}")
                                #print(f"3let:{word[2]}, blok:{blocks[c]}")
                                canSpell = True
        if not canSpell:
            print("NO")
        else:
            print("YES")
            canSpell = False

    if len(word) == 2:
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    for d in range(4):
                        if a != b and a != c and a != d and b != c and b != d and c != d:
                            #print(f"{a}, {b}, {c}, {d}")
                            if word[0] in blocks[a]:
                                if word[1] in blocks[b]:
                                            canSpell = True
        if not canSpell:
            print("NO")
        else:
            print("YES")
            canSpell = False

    if len(word) == 1:
        for block in blocks:
            if word[0] in block:
                canSpell = True
        if not canSpell:
            print("NO")
        else:
            print("YES")
            canSpell = False
