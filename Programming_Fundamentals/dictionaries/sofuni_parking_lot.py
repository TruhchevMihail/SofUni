entries = int(input())

parking = {}

for _ in range(entries):
    entry = input().split()
    command = entry[0]
    name = entry[1]

    if command == "register":
        plate = entry[2]
        if name in parking:
            print(f"ERROR: already registered with plate number {plate}")
        else:
            parking[name] = plate
            print(f'{name} registered {plate} successfully')

    elif command == "unregister":
        if name not in parking:
            print(f"ERROR: user {name} not found")
        else:
            parking.pop(name)
            print(f"{name} unregistered successfully")

for name, plate in parking.items():
    print(f"{name} => {plate}")