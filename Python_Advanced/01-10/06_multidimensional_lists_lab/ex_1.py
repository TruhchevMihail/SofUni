rows, columns = [int(el) for el in input().split(", ")]

matrix = []
sum_matrix = 0
for row_index in range(rows):
    row_data = [int(el) for el in input().split(", ")]
    sum_matrix += sum(row_data)
    matrix.append(row_data)

print(sum_matrix)
print(matrix)