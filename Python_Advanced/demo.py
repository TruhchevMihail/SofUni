import time
import os

# използва се за изчистване на екрана (работи в терминал)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Santa:
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }

    def __init__(self, presents, matrix):
        self.presents = presents
        self.matrix = matrix
        self.size = len(matrix)
        self.happy_kids = 0
        self.nice_kids = sum(row.count("V") for row in matrix)

        for r in range(self.size):
            for c in range(self.size):
                if matrix[r][c] == "S":
                    self.row, self.col = r, c

    def in_bounds(self, r, c):
        return 0 <= r < self.size and 0 <= c < self.size

    def move(self, direction):
        if direction not in self.directions:
            return

        d_row, d_col = self.directions[direction]
        next_r, next_c = self.row + d_row, self.col + d_col

        if not self.in_bounds(next_r, next_c):
            return

        current_cell = self.matrix[next_r][next_c]
        self.matrix[self.row][self.col] = "-"

        if current_cell == "V":
            self.presents -= 1
            self.happy_kids += 1
        elif current_cell == "C":
            self.feed_cookie(next_r, next_c)

        self.row, self.col = next_r, next_c
        self.matrix[self.row][self.col] = "S"

    def feed_cookie(self, r, c):
        for d in self.directions.values():
            adj_r, adj_c = r + d[0], c + d[1]
            if self.in_bounds(adj_r, adj_c) and self.presents > 0:
                cell = self.matrix[adj_r][adj_c]
                if cell == "V":
                    self.happy_kids += 1
                    self.presents -= 1
                    self.matrix[adj_r][adj_c] = "-"
                elif cell == "X":
                    self.presents -= 1
                    self.matrix[adj_r][adj_c] = "-"

    def display(self):
        clear()
        for row in self.matrix:
            print(" ".join(row))
        print(f"\n🎁 Presents left: {self.presents}")
        print(f"😊 Happy kids: {self.happy_kids}/{self.nice_kids}")
        time.sleep(0.5)

    def game_over(self):
        return self.presents == 0 or self.happy_kids == self.nice_kids


# === Вход ===
presents = int(input())
size = int(input())
matrix = [input().split() for _ in range(size)]

santa = Santa(presents, matrix)

# === Команди ===
while True:
    command = input()
    if command == "Christmas morning":
        break

    santa.move(command)
    santa.display()

    if santa.presents == 0:
        print("\nSanta ran out of presents!")
        break

# === Финален резултат ===
print()
for row in santa.matrix:
    print(" ".join(row))

if santa.happy_kids == santa.nice_kids:
    print(f"Good job, Santa! {santa.happy_kids} happy nice kid/s.")
else:
    print(f"No presents for {santa.nice_kids - santa.happy_kids} nice kid/s.")
