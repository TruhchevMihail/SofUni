current_string = input()

while True:
    command = input()
    if command == "End":
        break
    
    parts = command.split()
    action = parts[0]

    if action == "Translate":
        char = parts[1]
        replacment = parts[2]
        current_string = current_string.replace(char, replacment)
        print(current_string)

    elif action == "Includes":
        substring = parts[1]
        if substring in current_string:
            print("True")
        else:
            print("False")

    elif action == "Start":
        substring = parts[1]
        if current_string.startswith(substring):
            print("True")
        else:
            print("False")

    elif action == "Lowercase":
        current_string = current_string.lower()
        print(current_string)

    elif action == "FindIndex":
        char = parts[1]
        index = current_string.rfind(char)
        print(index)

    elif action == "Remove":
        start_index = int(parts[1])
        count = int(parts[2])
        current_string = current_string[:start_index] + current_string[start_index + count:]
        print(current_string)

