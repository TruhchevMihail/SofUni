def is_valid_index(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols

rows, cols = map(int, input().split())
matrix = [input().split() for _ in range(rows)]

while True:
    command = input()
    if command == "END":
        break

    parts = command.split()
    if (
        parts[0] == "swap"
        and len(parts) == 5
        and all(part.lstrip('-').isdigit() for part in parts[1:])
    ):
        r1, c1, r2, c2 = map(int, parts[1:])
        if (
            is_valid_index(r1, c1, rows, cols)
            and is_valid_index(r2, c2, rows, cols)
        ):
            matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
            for row in matrix:
                print(' '.join(row))
            continue

    print("Invalid input!")