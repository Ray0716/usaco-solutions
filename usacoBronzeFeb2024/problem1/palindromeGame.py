def is_palindrome(n):
    return str(n) == str(n)[::-1]


t = int(input())

testCases = []
for _ in range(t):
    testCases.append(int(input()))
for x in testCases:
    if is_palindrome(x):
        print("B")
        continue
    elif x > 10 and x < 21:
        print("B")
        continue
    else:
        print("E")
    


#t = int(input())

