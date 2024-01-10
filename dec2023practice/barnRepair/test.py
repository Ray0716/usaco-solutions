def sumOfLargest(list, largestNums):
    result = 0
    count = 0
    for x in range(len(list)):
        if count < largestNums:
            result += max(list)
            list.remove(max(list))
            count += 1
        else:
            return result
        
l = [1, 2, 2, 6, 1, 1, 1, 4, 4, 1, 1, 3, 1, 9, 1, 1, 1]

print(sumOfLargest(l, 4))