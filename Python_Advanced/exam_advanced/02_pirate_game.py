def pirate_quest():
    n = int(input())
    sea = [list(input()) for _ in range(n)]

    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }

    durability = 100
    charm_used = False
    treasure_count = sum(row.count('*') for row in sea)

    row, col = next((r, c) for r in range(n) for c in range(n) if sea[r][c] == 'S')

    def print_result(message):
        print(message)
        print(f"Ship Durability: {durability}")
        if treasure_count > 0:
            print(f"Unclaimed chests: {treasure_count}")
        sea[row][col] = 'S'
        for line in sea:
            print(''.join(line))

    while True:
        command = input()
        if command == 'stop':
            if treasure_count > 0:
                print_result("Retreat! Some treasures remain unclaimed.")
            else:
                print_result("Yo-ho-ho! All treasure chests collected!")
            return

        sea[row][col] = '.'
        d_row, d_col = directions[command]
        row = (row + d_row) % n
        col = (col + d_col) % n
        cell = sea[row][col]

        if cell == '*':
            treasure_count -= 1
            sea[row][col] = '.'
        elif cell == 'M':
            durability -= 25
            sea[row][col] = '.'
            if durability <= 0:
                print_result(f"Shipwreck! Last known coordinates ({row}, {col})")
                return
        elif cell == 'C':
            if not charm_used:
                durability = min(100, durability + 25)
                charm_used = True
            sea[row][col] = '.'

        if treasure_count == 0:
            print_result("Yo-ho-ho! All treasure chests collected!")
            return

pirate_quest()