necklace = ['r','r','r']

index = -1

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



print(substring1)
print(substring2)

e = ['a','b','c','d','e','f']
print(e[::-1])

try:
    print(e[100])
except IndexError:
    pass
print("awgjkluserf")