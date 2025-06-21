n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
bombs = input().split()

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

for bomb in bombs:
    r, c = map(int, bomb.split(','))
    bomb_value = matrix[r][c]
    if bomb_value > 0:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and matrix[nr][nc] > 0:
                matrix[nr][nc] -= bomb_value
        matrix[r][c] = 0

alive_cells = [cell for row in matrix for cell in row if cell > 0]
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
for row in matrix:
    print(' '.join(str(x) for x in row))