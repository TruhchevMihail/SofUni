rows, cols = map(int, input().split())
snake = input()

matrix = []
snake_idx = 0

for r in range(rows):
    row = []
    for c in range(cols):
        row.append(snake[snake_idx % len(snake)])
        snake_idx += 1
    if r % 2 == 1:
        row.reverse()
    matrix.append(row)

for row in matrix:
    print(''.join(row))