def pour(cap1, am1, cap2, am2):
    if am1 > (cap2 - am2):
        return [int(am1 - (cap2 - am2)), cap2]
    elif am1 == (cap2 - am2):
        return [0, cap2]
        print("OK")
    else:
        return [0, int(am1 + am2)]
        print("OK")

buckets = [[1,1],[1,1],[3,2]]

print(pour(1, 1, 3, 2))