rows, columns = [int(el) for el in input().split(", ")]

matrix = [0] * columns

for _ in range(rows):
    row_data = [int(el) for el in input().split()]
    for i in range(columns):
       matrix[i] += row_data[i]

print(*matrix, sep="\n")