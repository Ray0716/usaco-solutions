def can_visit_farms(N, Q, closing_times, travel_times, queries):
    closing_times.sort()
    travel_times.sort()
    
    for v, s in queries:
        count = 0
        i, j = 0, 0
        
        while i < N and j < N:
            arrival_time = s + travel_times[i]
            if arrival_time < closing_times[j]:
                count += 1
                i += 1
            j += 1
            
            if count >= v:
                print("YES")
                break
        else:
            print("NO")

# Reading input
N, Q = map(int, input().split())
closing_times = list(map(int, input().split()))
travel_times = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(Q)]

# Checking if Bessie can visit the farms based on each query
can_visit_farms(N, Q, closing_times, travel_times, queries)
