pumps = int(input())

matrix = [[int(x)for x in input().split()] for pump in range(pumps)]

start_index = 0
tank = 0
total = 0

for i in range(pumps):
    petrol, distance = matrix[i]

    tank += petrol - distance
    if tank < 0:
        start_index = i + 1
        total += tank
        tank = 0

if tank + total >= 0:
    print(start_index)
