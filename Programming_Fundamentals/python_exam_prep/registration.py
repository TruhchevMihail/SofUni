username = input()

while True:
    commands = input()
    if commands == "Registration":
        break

    command_parts = commands.split()
    command = command_parts[0]

    if command == "Letters":
        case = command_parts[1]
        if case == "Upper":
            username = username.upper()
            print(username)
        elif case == "Lower":
            username = username.lower()
            print(username)

    elif command == "Reverse":
        start_index = int(command_parts[1])
        end_index = int(command_parts[2])
        if 0 <= start_index < len(username) and 0 <= end_index < len(username):
            substring = username[start_index:end_index + 1]
            print(substring[::-1])
        else:
            continue

    elif command == "Substring":
        substring = command_parts[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}.")

    elif command == "Replace":
        char = command_parts[1]
        username = username.replace(char, "-")
        print(username)

    elif command == "IsValid":
        char = command_parts[1]
        if char in username:
            print("Valid username.")
        else:
            print(f"{char} must be contained in your username.")
