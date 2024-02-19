def roll_list(N, my_list):
    N = N % len(my_list)  # Handle cases where N is greater than the length of the list
    return my_list[N:] + my_list[:N]

with open('cbarn.in', 'r') as infile:
    n = int(infile.readline())
    data = []
    for _ in range(n):
        data.append(int(infile.readline()))

distances = []

for startIndex in range(n):
    barn = roll_list(startIndex, data)
    distances.append(sum([barn[x] * x for x in range(n)]))

with open('cbarn.out', 'w') as outfile:
    outfile.writelines(str(min(distances)))
