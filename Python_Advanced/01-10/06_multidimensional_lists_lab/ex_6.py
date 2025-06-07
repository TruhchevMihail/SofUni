matrix_size = int(input())

matrix = []

for _ in range(matrix_size):
    row_data = input()
    matrix.append(row_data)

symbol = input()

for i in range(matrix_size):
    for j in range(matrix_size):
        if matrix[i][j] == symbol:
            print(f"({i}, {j})")
            exit()
else:
    print(f"{symbol} does not occur in the matrix")