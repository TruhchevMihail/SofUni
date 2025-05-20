rows = int(input())

matrix = []

for row_index in range(rows):
    raw_data = [int(el)for el in input().split(", ")]
    matrix.append(raw_data[row_index] if row_index % 2 == 0 else None)

print(matrix)
