numTests = input()
numTests = int(numTests)
raw = []
arrays = []
a = []

for c in range(numTests * 2):
    raw.append(input())

for index in range(len(raw)):
    if index % 2 == 0:
        continue
    temp = []
    for num in raw[index].split():
        temp.append(int(num))

    a.append(temp)
    
def operate(array):
    l = len(array)
    m = 0
    res = []
    for x in range(l):
        if (2**l <= l):
            m += 1
        else:
            for index in range(l):
                if index <= 2**l:
                    array[index] -= 1

            return array                        

for testCase in a:                                                                  
    for c in range(100):
        g = testCase.sort(reverse = True)
        if operate(testCase) != g:
            testCase = operate(testCase)
        else:
            print("YES")
            continue
        print("NO")