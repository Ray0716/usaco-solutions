def count_lists_with_minus_one(list_of_lists):
    count = 0
    for sublist in list_of_lists:
        if sublist[0] == -1:
            count += 1
    return count




print(count_lists_with_minus_one([[0, 1], [-1, 1], [1, 2], [0, 1], [1, 1]]))