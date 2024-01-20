def swap(indexA, indexB, list):
    temp = list[indexA - 1]
    list[indexA - 1] = list[indexB - 1]
    list[indexB - 1] = temp

with open('shell.in', 'r') as infile:
    n = int(infile.readline())
    data = []
    for _ in range(n):
        data.append([int(x) for x in infile.readline().split()])


correctGuessesForEachPosition = []
for x in range(3):
    shells = ["", "", ""]
    shells[x] = "*"
    correctGuessesForThisPosition = 0
    for guess in data:
        swap(guess[0], guess[1], shells)
        if shells[guess[2] - 1] == "*":
            correctGuessesForThisPosition += 1
    
    correctGuessesForEachPosition.append(correctGuessesForThisPosition)

with open('shell.out', 'w') as outfile:
    outfile.write(str(max(correctGuessesForEachPosition)))

