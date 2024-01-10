def find_minimum(lst):
    # Find the minimum value in the list
    

    return min(lst)


def find_second_minimum(lst):
    # Find the second minimum value by excluding the minimum
    min_value = min(lst)
    second_min_value = min(value for value in lst if value != min_value)

    return second_min_value

t = int(input())

testCases = []
for x in range(t):
    testCases.append([int(input()), [int(y) for y in input().split()]])

for testCase in testCases:
    allTheSame = False
    modifications = 0
    n = testCase[0]
    sleepLog = testCase[1]
    print(sleepLog)
    while allTheSame == False:
        for sleepIndex in range(len(sleepLog)-1): #track pair of adjacent sleeps
            if len(set(sleepLog)) == 1: # if aLL ELEMETN same, we immediatelky output 0
                print(modifications)
                allTheSame = True
                break # stop iterating over pairs
            elif(sleepLog[sleepIndex] == min(sleepLog) and sleepLog[sleepIndex + 1] == find_second_minimum(sleepLog)) or (sleepLog[sleepIndex] == find_second_minimum(sleepLog) and sleepLog[sleepIndex + 1] == min(sleepLog)):
                # change second one to the sum, delete first
                sleepLog[sleepIndex+1] = sleepLog[sleepIndex] + sleepLog[sleepIndex+1]
                del sleepLog[sleepIndex]
                print("merged two thigns")
                break


