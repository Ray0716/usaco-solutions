with open('infile.in', 'r') as infile:
    lines = infile.readlines()
    data = []
    for line in lines:
        row = [int(x) for x in line.strip().split(" ")] # if each line has integers
        data.append(line.split()) # if line is string

        # line is a string
        
with open('outfile.out', 'w') as outFile:
    outFile.write(" hello world")


# if in/out is stdin stdout:


numIn = input()
numIn = int(numIn)
inputs = []

for x in range(numIn):
    inputs.append(input())