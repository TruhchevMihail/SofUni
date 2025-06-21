size = int(input())
commands = input().split()
field = [input().split() for _ in range(size)]

miner_row, miner_col = 0, 0
total_coal = 0

for r in range(size):
    for c in range(size):
        if field[r][c] == 's':
            miner_row, miner_col = r, c
        elif field[r][c] == 'c':
            total_coal += 1

collected = 0
directions = {
    "up":    (-1, 0),
    "down":  (1, 0),
    "left":  (0, -1),
    "right": (0, 1)
}

for cmd in commands:
    dr, dc = directions[cmd]
    nr, nc = miner_row + dr, miner_col + dc

    if 0 <= nr < size and 0 <= nc < size:
        miner_row, miner_col = nr, nc
        cell = field[miner_row][miner_col]
        if cell == 'c':
            collected += 1
            field[miner_row][miner_col] = '*'
            if collected == total_coal:
                print(f"You collected all coal! ({miner_row}, {miner_col})")
                break
        elif cell == 'e':
            print(f"Game over! ({miner_row}, {miner_col})")
            break
else:
    print(f"{total_coal - collected} pieces of coal left. ({miner_row}, {miner_col})")