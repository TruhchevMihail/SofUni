from collections import deque

green_light = int(input())
free_window = int(input())

cars = deque()
cars_passed = 0

while True:
    command = input()
    if command == "END":
        print("Everyone is safe.")
        print(f"{cars_passed} total cars passed the crossroads.")
        break
    elif command == "green":
        time_left = green_light
        while cars and time_left > 0:
            car = cars.popleft()
            car_length = len(car)
            if car_length <= time_left:
                time_left -= car_length
                cars_passed += 1
            else:
                remaining = car_length - time_left
                if remaining <= free_window:
                    cars_passed += 1
                    time_left = 0
                else:
                    hit_index = time_left + free_window
                    print("A crash happened!")
                    print(f"{car} was hit at {car[hit_index]}.")
                    exit()
    else:
        cars.append(command)