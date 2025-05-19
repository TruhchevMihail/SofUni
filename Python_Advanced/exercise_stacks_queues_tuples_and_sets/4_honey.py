from collections import deque


working_bee = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbol = input().split()

honey = 0

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y != 0 else 0
}

while working_bee and nectar:
    if nectar[-1] >= working_bee[0]:
        honey += abs(operations[symbol[0]](working_bee[0], nectar[-1]))
        working_bee.popleft()
        nectar.pop()
        symbol.pop(0)
    else:
        nectar.pop()

print(f"Total honey made: {honey}")

if working_bee:
    print(f"Bees left: {', '.join(str(x) for x in working_bee)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
