import os

while True:
    line = input()
    if line == "End":
        break
 
    command, file_name, *args = line.split("-")

    if command == "Create":
        with open(file_name, "w") as file:
            pass

    elif command == "Add":
        content = args[0]
        with open(file_name, "a") as file:
            file.write(content + "\n")

    elif command == "Replace":
        old_string, new_string = args
        try:
            with open(file_name, "r") as file:
                text = file.read()
            text = text.replace(old_string, new_string)
            with open(file_name, "w") as file:
                file.write(text)
        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")