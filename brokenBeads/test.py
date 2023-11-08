necklace = [0,1,2,3,4,5,6,7,8,9,10]

index = 4

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
