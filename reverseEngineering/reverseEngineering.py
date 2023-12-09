class testCase:
    def __init__(self, inputs, outputs, n, m): #in out list of strings
        self.inputs = inputs
        self.outputs = outputs
        self.n = n
        self.m = m

def returnAllIndexes(ls, index):
    result = []
    for element in ls:
        result.append(element[index])
    return result

def isAllEqual(lst):
    try:
        return lst.count(lst[0]) == len(lst)
    except:
        return True

def readCase():
    inp = []
    out = []
    newline = input()
    nm = input()

    
    nm = [int(c) for c in nm.split()]
    n = nm[0]
    m = nm[1]
    for x in range(m):
        line = input()
        line = line.split()
        inp.append(line[0])
        out.append(int(line[1]))
    
    return testCase(inp, out, n, m)


data = []
c = 0
for x in range(int(input())):
    data.append(readCase())
    

for x in data:
    print(f"inp: {x.inputs}, out:{x.outputs}, n:{x.n}, m{x.m}")


for c in data:
    for i in range(0, len(c.inputs)):
        c.inputs[i] = [int(ele) for ele in c.inputs[i].split()]




for testc in data:
    for varIndex in range(testc.n): #checking each index in the input to see if there are deciding vars
        inList = returnAllIndexes(testc.inputs, varIndex)
        zeroes = []
        ones = []
        outZeroes = []
        outOnes = []

        for x in range(len(inList)): # compare input and output
            if inList[x] == 0:
                zeroes.append(x) #inlist is vertical scan of the inputs all of the same index
            elif inList[x] == 1: # zeres and ones is list of index of all the zeroes and ones in teh vertical slice
                ones.append(x)

        for y in zeroes:
            if testc.outputs[y] == 0:
                outZeroes.append(y) # indexes of output 0's and 1's
            elif testc.outputs[y] == 1:
                outOnes.append(y)

        for x in testc.inputs:
            test = []
            for y in outZeroes:
                test.append(x[y])
            
            if isAllEqual(test):
                for x in testc.inputs:
                    for y in outZeroes:
                        testc.inputs.remove(testc.inputs[y])

        for x in testc.inputs:
            test = []
            for y in outOnes:
                test.append(x[y])
            
            if isAllEqual(test):
                for x in testc.inputs:
                    for y in outOnes:
                        testc.inputs.remove(testc.inputs[y])

    


for testc in data:
    for varIndex in range(testc.n): #checking each index in the input to see if there are deciding vars
        inList = returnAllIndexes(testc.inputs, varIndex)
        zeroes = []
        ones = []
        outZeroes = []
        outOnes = []

        for x in range(len(inList)): # compare input and output
            if inList[x] == 0:
                zeroes.append(x) #inlist is vertical scan of the inputs all of the same index
            elif inList[x] == 1: # zeres and ones is list of index of all the zeroes and ones in teh vertical slice
                ones.append(x)

        for y in zeroes:
            if testc.outputs[y] == 0:
                outZeroes.append(y) # indexes of output 0's and 1's
            elif testc.outputs[y] == 1:
                outOnes.append(y)

        for x in testc.inputs:
            test = []
            for y in outZeroes:
                test.append(x[y])
            
            if isAllEqual(test):
                for x in testc.inputs:
                    for y in outZeroes:
                        testc.inputs.remove(testc.inputs[y])

        for x in testc.inputs:
            test = []
            for y in outOnes:
                test.append(x[y])
            
            if isAllEqual(test):
                for x in testc.inputs:
                    for y in outOnes:
                        testc.inputs.remove(testc.inputs[y])



for tc in data:
    if len(tc.inputs) == 0:
        print("OK")
    else:
        print("LIE")

            