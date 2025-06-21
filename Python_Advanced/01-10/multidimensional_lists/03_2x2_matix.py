rows, cols = map(int, input().split())
matrix = [input().split() for _ in range(rows)]

count = 0

for r in range(rows - 1):
    for c in range(cols - 1):
        char = matrix[r][c]
        if (
            char == matrix[r][c + 1]
            and char == matrix[r + 1][c]
            and char == matrix[r + 1][c + 1]
        ):
            count += 1

print(count)