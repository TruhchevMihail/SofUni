n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

while True:
    command = input()
    if command == "END":
        break

    parts = command.split()
    action = parts[0]
    row, col, value = map(int, parts[1:])

    if 0 <= row < n and 0 <= col < len(matrix[row]):
        if action == "Add":
            matrix[row][col] += value
        elif action == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

for row in matrix:
    print(' '.join(map(str, row)))