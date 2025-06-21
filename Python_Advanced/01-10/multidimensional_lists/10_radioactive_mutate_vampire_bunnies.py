rows, cols = map(int, input().split())
lair = [list(input()) for _ in range(rows)]
commands = input()

for r in range(rows):
    for c in range(cols):
        if lair[r][c] == 'P':
            player_pos = (r, c)
            break

directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

def spread_bunnies(lair):
    new_bunnies = []
    for r in range(rows):
        for c in range(cols):
            if lair[r][c] == 'B':
                for dr, dc in directions.values():
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if lair[nr][nc] != 'B':
                            new_bunnies.append((nr, nc))
    for r, c in new_bunnies:
        lair[r][c] = 'B'

won = False
dead = False
last_pos = player_pos # type: ignore

for cmd in commands:
    pr, pc = player_pos # type: ignore
    dr, dc = directions[cmd]
    nr, nc = pr + dr, pc + dc

    lair[pr][pc] = '.'
    if not (0 <= nr < rows and 0 <= nc < cols):
        spread_bunnies(lair)
        won = True
        last_pos = (pr, pc)
        break
    if lair[nr][nc] == 'B':
        player_pos = (nr, nc)
        spread_bunnies(lair)
        dead = True
        last_pos = (nr, nc)
        break
    player_pos = (nr, nc)
    lair[nr][nc] = 'P'
    spread_bunnies(lair)
    if lair[nr][nc] == 'B':
        dead = True
        last_pos = (nr, nc)
        break

for row in lair:
    print(''.join(row))
if won:
    print(f"won: {last_pos[0]} {last_pos[1]}")
elif dead:
    print(f"dead: {last_pos[0]} {last_pos[1]}")