rows, cols = map(int, input().split())

for r in range(rows):
    row = []
    for c in range(cols):
        first_last = chr(ord('a') + r)
        middle = chr(ord('a') + r + c)
        palindrome = first_last + middle + first_last
        row.append(palindrome)
    print(' '.join(row))