def is_valid(r, c, n):
    return 0 <= r < n and 0 <= c < n

def count_attacks(board, row, col, n):
    moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    attacks = 0
    for dr, dc in moves:
        nr, nc = row + dr, col + dc
        if is_valid(nr, nc, n) and board[nr][nc] == "K":
            attacks += 1
    return attacks

n = int(input())
board = [list(input()) for _ in range(n)]
removed = 0

while True:
    max_attacks = 0
    knight_pos = None

    for r in range(n):
        for c in range(n):
            if board[r][c] == "K":
                attacks = count_attacks(board, r, c, n)
                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_pos = (r, c)

    if max_attacks == 0:
        break

    r, c = knight_pos # type: ignore
    board[r][c] = "0"
    removed += 1

print(removed)