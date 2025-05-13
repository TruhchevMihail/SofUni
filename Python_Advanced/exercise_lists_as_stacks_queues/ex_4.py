cloths = [int(x) for x in input().split()]
rack_capacity = int(input())

racks = 0

while cloths:
    racks += 1
    current_rack = rack_capacity
    while current_rack > 0 and cloths:
        if current_rack >= cloths[-1]:
            current_rack -= cloths.pop()
        else:
            break

print(racks)
