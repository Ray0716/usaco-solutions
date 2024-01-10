# Function to rotate a stamp pattern 90 degrees clockwise
def rotate_stamp(pattern):
    n = len(pattern)
    rotated = [['.'] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = pattern[i][j]
    return [''.join(row) for row in rotated]

# Function to check if a stamp pattern can match the desired painting
def can_create_painting(N, painting, K, stamp):
    for _ in range(4):  # Try all four possible rotations
        for i in range(N - K + 1):
            for j in range(N - K + 1):
                match = True
                for si in range(K):
                    for sj in range(K):
                        if stamp[si][sj] == '*' and painting[i + si][j + sj] == '.':
                            match = False
                            break
                    if not match:
                        break
                if match:
                    return True
        stamp = rotate_stamp(stamp)  # Rotate the stamp pattern

    return False

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    N = int(input())
    painting = [input() for _ in range(N)]
    K = int(input())
    stamp = [input() for _ in range(K)]

    # Check if Bessie can create the desired stamp painting
    if can_create_painting(N, painting, K, stamp):
        print("YES")
    else:
        print("NO")
