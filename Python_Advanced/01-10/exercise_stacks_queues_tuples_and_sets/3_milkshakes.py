from collections import deque


chocolates = [int(x) for x in input().split(", ")]
cup_of_milks = deque(int(x) for x in input().split(", "))
milkshakes = 0

while chocolates and cup_of_milks and milkshakes < 5:

    if chocolates[-1] <= 0 and cup_of_milks[0] <= 0:
        chocolates.pop()
        cup_of_milks.popleft()
        continue
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    if cup_of_milks[0] <= 0:
        cup_of_milks.popleft()
        continue
    
    if chocolates[-1] == cup_of_milks[0]:
        milkshakes += 1
        chocolates.pop()
        cup_of_milks.popleft()
    else:
        cup_of_milks.rotate(-1)
        chocolates[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print("Chocolate: " + ', '.join(str(x) for x in chocolates))
else:
    print("Chocolate: empty")

if cup_of_milks:
    print("Milk: " + ", ".join(str(x) for x in cup_of_milks))
else:
    print("Milk: empty")