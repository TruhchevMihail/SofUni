size = int(input())
field = [input().split() for _ in range(size)]

bunny_row, bunny_col = 0, 0
for r in range(size):
    for c in range(size):
        if field[r][c] == "B":
            bunny_row, bunny_col = r, c

directions = {
    "up":    (-1, 0),
    "down":  (1, 0),
    "left":  (0, -1),
    "right": (0, 1)
}

best_direction = ""
best_path = []
max_eggs = float('-inf')

for direction, (dr, dc) in directions.items():
    eggs = 0
    path = []
    row, col = bunny_row + dr, bunny_col + dc
    while 0 <= row < size and 0 <= col < size:
        if field[row][col] == "X":
            break
        eggs += int(field[row][col])
        path.append([row, col])
        row += dr
        col += dc
    if eggs > max_eggs and path:
        max_eggs = eggs
        best_direction = direction
        best_path = path

print(best_direction)
for pos in best_path:
    print(pos)
print(max_eggs)