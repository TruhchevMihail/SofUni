from collections import deque


kid_names = input().split()
n = int(input())

kids = deque(kid_names)

while len(kids) > 1:
    kids.rotate(-(n - 1))

    removed_kid = kids.popleft()
    print(f"Removed {removed_kid}")

print(f"Last is {kids[0]}")
