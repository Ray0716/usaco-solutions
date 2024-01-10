def min_starting_infected_cows(N, bitstring):
    min_infected_cows = float('inf')
    total_infected = bitstring.count('1')

    for i in range(N):
        infected_count = bitstring[i:].count('1') + bitstring[:i].count('1')
        min_infected_cows = min(min_infected_cows, max(infected_count, total_infected))

    return min_infected_cows

# Reading input
N = int(input())
bitstring = input().strip()

# Calculating and printing the result
result = min_starting_infected_cows(N, bitstring)
print(result)