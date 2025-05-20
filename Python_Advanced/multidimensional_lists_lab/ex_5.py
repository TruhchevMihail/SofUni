rows = int(input())

matrix = []


for _ in range(rows):
    row_data = [int(el) for el in input().split()]
    matrix.append(row_data)

sum_matrix = 0
for i in range(rows):
    sum_matrix += matrix[i][i]

print(sum_matrix)

