rows = int(input())

matrix = []

for row_index in range(rows):
    row_data = [int(el) for el in input().split(",")]
    matrix.extend(row_data)

print(matrix)