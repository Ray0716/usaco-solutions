def remove_duplicates(lst):
    for x in range(len(lst)):
        if len(lst[x]) == 2:
            lst[x] = lst[x][0] + lst[x][1]
        else:
            lst[x] = lst[x][0]
    print(lst)

    return list(set(lst))

print(remove_duplicates([['C', 'A'], ['B', 'A'], ['B'], ['B', 'A'], ['A'], ['B', 'A']]))
