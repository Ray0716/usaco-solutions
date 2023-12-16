def pour_milk(capacities, amounts):
    for i in range(100):
        # Determine the current bucket and the next bucket
        current = i % 3
        next_bucket = (i + 1) % 3

        # Pour from current bucket to next bucket
        amount_poured = min(amounts[current], capacities[next_bucket] - amounts[next_bucket])
        amounts[current] -= amount_poured
        amounts[next_bucket] += amount_poured

    return amounts

# Bucket capacities and initial amounts
capacities = [10, 11, 12]  # Capacities of the buckets
amounts = [3, 4, 5]  # Initial milk amounts in each bucket

b = []

with open('mixmilk/mixmilk.in', 'r') as inFile:
    for x in range(3):
        b.append([int(x) for x in inFile.readline().split()])


# Calculate the final amounts after 100 pours
final_amounts = pour_milk(capacities, amounts)
print(final_amounts)