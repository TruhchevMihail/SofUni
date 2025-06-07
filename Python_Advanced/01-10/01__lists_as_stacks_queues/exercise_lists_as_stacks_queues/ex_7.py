from collections import deque
from datetime import datetime, timedelta

robots_input = input().split(";")
robots = []
for robot in robots_input:
    name, time = robot.split("-")
    robots.append({"name": name, "process_time": int(time), "available_at": 0})

start_time = datetime.strptime(input(), "%H:%M:%S")
current_time = 0

products = deque()
while True:
    product = input()
    if product == "End":
        break
    products.append(product)

waiting_products = deque(products)
robots_count = len(robots)
robot_busy = [0] * robots_count

while waiting_products:
    current_time += 1
    product = waiting_products.popleft()
    assigned = False

    for i in range(robots_count):
        if robot_busy[i] > 0:
            robot_busy[i] -= 1

    for i in range(robots_count):
        if robot_busy[i] == 0:
            robot_busy[i] = robots[i]["process_time"]
            process_time = start_time + timedelta(seconds=current_time)
            print(f"{robots[i]['name']} - {product} [{process_time.strftime('%H:%M:%S')}]")
            assigned = True
            break

    if not assigned:
        waiting_products.append(product)