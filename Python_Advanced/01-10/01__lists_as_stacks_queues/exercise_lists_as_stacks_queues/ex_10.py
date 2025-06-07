from collections import deque

cups = deque(map(int, input().split()))
bottles = list(map(int, input().split()))

wasted_water = 0

while cups and bottles:
    current_cup = cups[0]
    current_bottle = bottles.pop()
    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
        cups.popleft()
    else:
        cups[0] -= current_bottle

if not cups:
    print(f"Bottles: {' '.join(map(str, reversed(bottles)))}")
else:
    print(f"Cups: {' '.join(map(str, cups))}")

print(f"Wasted litters of water: {wasted_water}")