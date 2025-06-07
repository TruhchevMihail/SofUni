from collections import deque

food_quantity = int(input())
orders = deque(map(int, input().split()))

print(max(orders))

while orders:
    if food_quantity >= orders[0]:
        food_quantity -= orders.popleft()
    else:
        print("Orders left:", *orders)
        break

if not orders:
    print("Orders complete")