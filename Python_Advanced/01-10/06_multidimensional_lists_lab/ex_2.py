rows = int(input())

matrix = []

for row_index in range(rows):
    raw_data = [int(el)for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(raw_data)

print(matrix)
