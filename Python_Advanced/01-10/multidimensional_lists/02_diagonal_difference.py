n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

primary_sum = sum(matrix[i][i] for i in range(n))
secondary_sum = sum(matrix[i][n - 1 - i] for i in range(n))

print(abs(primary_sum - secondary_sum))