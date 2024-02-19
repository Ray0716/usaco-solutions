n = int(input())
data = [int(x) for x in input().split()]
print(data)
even = 0
odd = 0
for cow in data:
    if cow % 2 == 0:
        even += 1
    else:
        odd += 1

groupNums = 0
#even+even, even+odd
print(even, odd)
thisGroupEven = True
while not(even <= 0 and odd <= 0):
    if thisGroupEven:
        thisGroupEven = False
        if even > odd:
            even -= 1
            if not(even <= 0 and odd <= 0):
                groupNums += 1
        else:
            odd -= 2
            if not(even <= 0 and odd <= 0):
                groupNums += 1
        #if not(even <= 0 and odd <= 0):
            #groupNums += 1
    else:
        thisGroupEven = True
        if even >= 1 and odd >= 1:
            even -= 1
            odd -= 1
            if not(even <= 0 and odd <= 0):
                groupNums += 1
        else:
            odd -= 3
            if not(even <= 0 and odd <= 0):
                groupNums += 1
        #if not(even <= 0 and odd <= 0):
            #groupNums += 1

print(groupNums)

    
