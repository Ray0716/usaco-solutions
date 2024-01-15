global letterNumber
letterNumber = {chr(i + ord('a')): i for i in range(26)}

def findLettersForBoard(board):
    # board = [['a', 'b', 'c'], ['d', 'e', 'f']]
    numOfLettersOne = [0] * 26
    numOfLettersTwo = [0] * 26
    for letter in board[0]:
        numOfLettersOne[letterNumber[letter]] += 1
    
    for letter in board[1]:
        numOfLettersTwo[letterNumber[letter]] += 1

    result = []
    for x in range(26):
        result.append(max(numOfLettersOne[x], numOfLettersTwo[x]))
    
    return result
    


with open('blocks.in', 'r') as infile:
    n = int(infile.readline())
    data = []
    for x in range(n):
        data.append([[*x] for x in infile.readline().split()])

#print(data)
        
result = [0] * 26

for board in data:
    result = [x + y for x, y in zip(result, findLettersForBoard(board))]

with open('blocks.out', 'w') as outfile:
    for x in result:
        outfile.write(str(x))
        outfile.write("\n")