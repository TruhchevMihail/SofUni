starting_liters = int(input())

queue = []

while True:
    names = input()
    if names == "Start":
        break
    queue.append(names)

while True:
    command = input()
    if command == "End":
        print(f"{starting_liters} liters left")
        break

    if command.startswith("refill"):
        _, liters = command.split()
        starting_liters += int(liters)
    else:
        liters_needed = int(command)
        person = queue.pop(0)
        if starting_liters >= liters_needed:
            starting_liters -= liters_needed
            print(f"{person} got water")
        else:
            print(f"{person} must wait")