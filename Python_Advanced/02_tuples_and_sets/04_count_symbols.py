text = input()
char_counts = {}

for char in text:
    if char not in char_counts:
        char_counts[char] = 0
    char_counts[char] += 1

for char in sorted(char_counts):
    print(f"{char}: {char_counts[char]} time/s")