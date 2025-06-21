def range_day_simulation(field, commands):
    def in_range(r, c):
        return 0 <= r < 5 and 0 <= c < 5

    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    player_row, player_col = 0, 0
    targets = 0
    for r in range(5):
        for c in range(5):
            if field[r][c] == "A":
                player_row, player_col = r, c
            elif field[r][c] == "x":
                targets += 1

    shot_targets = []

    for command in commands:
        parts = command.split()
        action = parts[0]
        direction = parts[1]

        if action == "move":
            steps = int(parts[2])
            dr, dc = directions[direction]
            next_row, next_col = player_row, player_col
            valid = True
            for _ in range(steps):
                next_row += dr
                next_col += dc
                if not in_range(next_row, next_col) or field[next_row][next_col] != ".":
                    valid = False
                    break
            if valid:
                field[player_row][player_col] = "."
                player_row, player_col = next_row, next_col
                field[player_row][player_col] = "A"

        elif action == "shoot":
            dr, dc = directions[direction]
            row, col = player_row + dr, player_col + dc
            while in_range(row, col):
                if field[row][col] == "x":
                    shot_targets.append([row, col])
                    field[row][col] = "."
                    targets -= 1
                    break
                row += dr
                col += dc
            if targets == 0:
                break

    result = []
    if targets == 0:
        result.append(f"Training completed! All {len(shot_targets)} targets hit.")
    else:
        result.append(f"Training not completed! {targets} targets left.")
    result.extend([str(t) for t in shot_targets])
    return "\n".join(result)
