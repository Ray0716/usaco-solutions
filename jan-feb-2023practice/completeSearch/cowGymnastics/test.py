def elements_after(lst, element):
    try:
        index = lst.index(element)
        result = lst[index + 1:]
        result.sort()
        return result
    except ValueError:
        return []

def list_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = list(set1 & set2)
    intersection.sort()
    return intersection


a = [2,3]
b = [3]
print(elements_after(a, 1))