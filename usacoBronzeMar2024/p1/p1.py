def andOp(str1, str2):
    if str1 == "true" and str2 == "true":
        return "true"
    else:
        return "false"
    
def orOp(str1, str2):
    if str1 == "false" and str2 == "false":
        return "false"
    else:
        return "true"

def replace_range_with_element(lst, start, end, replacement):
    res = []
    for x in lst[:start-1]:
        res.append(x)
    res.append(replacement)
    for x in lst[end:]:
        res.append(x)
    return res

def eval(strlst):

    #print(strlst)
    #print(strlst)
    andresult = []
    for index in range(len(strlst)):
        if index % 2 != 0: #operator
            #print(index)
            if strlst[index] == "and":
                andresult.append(andOp(strlst[index - 1], strlst[index + 1]))
            elif strlst[index] == "or":
                andresult.append("or")
            index += 2
            andresult.pop(len(andresult) - 2)
        else:
            andresult.append(strlst[index])

    if "true" in andresult: # in a bool operation of only or's one true = all true
        return True
    else:
        return False

#print(eval("false and true or true"))
                

nq = [int(x) for x in input().split()]
n = nq[0]
q = nq[1]
boolstr = input().split()
queries = []
for x in range(q):
    temp = input().split()
    temp[0] = int(temp[0])
    temp[1] = int(temp[1])
    queries.append(temp)

resList = []

for qu in queries:
    # first try true
    i1 = qu[0]
    i2 = qu[1]
    tempT = replace_range_with_element(boolstr, i1, i2, "true") # when replce range with t
    #print(tempT)
    tempF = replace_range_with_element(boolstr, i1, i2, "false") # when replace r with f
    #print(tempF)

    eT = eval(tempT)
    eF = eval(tempF)

    if qu[2] == "true":
        if eT is True or eF is True:
            resList.append("Y")
        else:
            resList.append("N")
    elif qu[2] == "false":
        if eT is False or eF is False:
            resList.append("Y")
        else:
            resList.append("N")

print("".join(resList))


    

