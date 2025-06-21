def in_range(r, c):
    return 0 <= r < 5 and 0 <= c < 5

def move_player(row, col, direction, steps, field):
    dr, dc = directions[direction]
    for _ in range(steps):
        row += dr
        col += dc
        if not in_range(row, col) or field[row][col] != ".":
            return None 
    return row, col

def shoot(row, col, direction, field):
    dr, dc = directions[direction]
    row += dr
    col += dc
    while in_range(row, col):
        if field[row][col] == "x":
            field[row][col] = "."
            return [row, col]
        row += dr
        col += dc
    return None

field = [input().split() for _ in range(5)]

player_row, player_col = 0, 0
targets = 0
for r in range(5):
    for c in range(5):
        if field[r][c] == "A":
            player_row, player_col = r, c
        elif field[r][c] == "x":
            targets += 1

directions = {
    "up":    (-1, 0),
    "down":  (1, 0),
    "left":  (0, -1),
    "right": (0, 1)
}

n = int(input())
shot_targets = []

for _ in range(n):
    parts = input().split()
    command = parts[0]
    direction = parts[1]

    if command == "move":
        steps = int(parts[2])
        result = move_player(player_row, player_col, direction, steps, field)
        if result:
            player_row, player_col = result

    elif command == "shoot":
        result = shoot(player_row, player_col, direction, field)
        if result:
            shot_targets.append(result)
            targets -= 1
            if targets == 0:
                break

if targets == 0:
    print(f"Training completed! All {len(shot_targets)} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")
for t in shot_targets:
    print(t)