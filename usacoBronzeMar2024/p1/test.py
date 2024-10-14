def replace_range_with_element(lst, start, end, replacement):
    res = []
    for x in lst[:start-1]:
        res.append(x)
    res.append(replacement)
    for x in lst[end:]:
        res.append(x)
    return res

lst = [1, 2, 3, 4, 5, 6]

print(replace_range_with_element(lst, 3, 5, 123947685))