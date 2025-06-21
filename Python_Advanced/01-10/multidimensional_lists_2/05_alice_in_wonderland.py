n = int(input())
matrix = [input().split() for _ in range(n)]

alice_row, alice_col = 0, 0
for r in range(n):
    for c in range(n):
        if matrix[r][c] == "A":
            alice_row, alice_col = r, c

tea_collected = 0
directions = {
    "up":    (-1, 0),
    "down":  (1, 0),
    "left":  (0, -1),
    "right": (0, 1)
}

matrix[alice_row][alice_col] = "*"

while tea_collected < 10:
    command = input()
    dr, dc = directions[command]
    alice_row += dr
    alice_col += dc

    if not (0 <= alice_row < n and 0 <= alice_col < n):
        print("Alice didn't make it to the tea party.")
        break

    if matrix[alice_row][alice_col] == "R":
        matrix[alice_row][alice_col] = "*"
        print("Alice didn't make it to the tea party.")
        break

    if matrix[alice_row][alice_col].isdigit():
        tea_collected += int(matrix[alice_row][alice_col])

    matrix[alice_row][alice_col] = "*"
else:
    print("She did it! She went to the party.")

for row in matrix:
    print(' '.join(row))