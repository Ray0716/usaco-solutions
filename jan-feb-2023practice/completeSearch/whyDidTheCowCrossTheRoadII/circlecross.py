def find_first_second_occurrences(lst, target_element):
    first_index = None
    second_index = None

    for index, element in enumerate(lst):
        if element == target_element:
            if first_index is None:
                first_index = index
            else:
                second_index = index
                break  # Break the loop after finding the second occurrence

    return[first_index, second_index]

def remove_duplicates(input_list):
    unique_list = []

    for sublist in input_list:
        if sublist not in unique_list:
            unique_list.append(sublist)

    return unique_list

def find_unique_elements(lst):
    element_counts = {}
    
    # Count occurrences of each element
    for element in lst:
        if element in element_counts:
            element_counts[element] += 1
        else:
            element_counts[element] = 1
    
    # Filter elements that appear only once
    unique_elements = [element for element, count in element_counts.items() if count == 1]
    
    return unique_elements

def isFirstElement(list, index):
    y = list[index]
    for x in list[:index]:
        if x == y:
            return False # the input index is the second occurence of the element
    return True 

with open('circlecross.in', 'r') as infile:
    data = [x for x in infile.readline()]
    try:
        data.remove("\n")
    except:
        pass

pairs = []

for cowIndex in range(52):
    if isFirstElement(data, cowIndex):
        # print(data[cowIndex], find_first_second_occurrences(data, data[cowIndex]))
        for cow in find_unique_elements(data[find_first_second_occurrences(data, data[cowIndex])[0] + 1:find_first_second_occurrences(data, data[cowIndex])[1]]):
            pairs.append([data[cowIndex], cow])
for x in pairs:
    x.sort()
pairs = remove_duplicates(pairs)

with open('circlecross.out', 'w') as outfile:
    outfile.write(str(len(pairs)))

