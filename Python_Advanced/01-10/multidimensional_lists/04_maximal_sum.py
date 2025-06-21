rows, cols = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(rows)]

max_sum = float('-inf')
max_square = []

for r in range(rows - 2):
    for c in range(cols - 2):
        current_square = [matrix[r + i][c:c + 3] for i in range(3)]
        current_sum = sum(sum(row) for row in current_square)
        if current_sum > max_sum:
            max_sum = current_sum
            max_square = current_square

print(f"Sum = {max_sum}")
for row in max_square:
    print(' '.join(map(str, row)))