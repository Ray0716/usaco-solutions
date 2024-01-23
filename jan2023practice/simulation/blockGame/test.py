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
