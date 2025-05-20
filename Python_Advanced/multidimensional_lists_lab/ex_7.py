rows, columns = [int(el) for el in input().split(", ")]

matrix = [ [int(el) for el in input().split(", ")] for _ in range(rows) ]

max_sum = float('-inf')
best_row = 0
best_col = 0

for row in range(rows - 1):
    for col in range(columns - 1):
        current_sum = (
            matrix[row][col] + matrix[row][col + 1] +
            matrix[row + 1][col] + matrix[row + 1][col + 1]
        )
        if current_sum > max_sum:
            max_sum = current_sum
            best_row = row
            best_col = col

print(f"{matrix[best_row][best_col]} {matrix[best_row][best_col + 1]}")
print(f"{matrix[best_row + 1][best_col]} {matrix[best_row + 1][best_col + 1]}")
print(max_sum)
