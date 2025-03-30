trip = input()

while True:
    command = input()
    if command == "Travel":
        print(f"Ready for world tour! Planned stops: {trip}")
        break

    parts = command.split(":")
    action = parts[0]

    if action == "Add Stop":
        if len(parts) == 3:
            index = int(parts[1])
            new_stop = parts[2]

            if 0 <= index <= len(trip):
                trip = trip[:index] + new_stop + trip[index:]
        print(trip)

    elif action == "Remove Stop":
        if len(parts) == 3:
            start_index = int(parts[1])
            end_index = int(parts[2])

            if 0 <= start_index <= end_index < len(trip):
                trip = trip[:start_index] + trip[end_index + 1:]
        print(trip)

    elif action == "Switch":
        if len(parts) == 3:
            old_string = parts[1]
            new_string = parts[2]

            if old_string and old_string in trip:
                trip = trip.replace(old_string, new_string)
        print(trip)
