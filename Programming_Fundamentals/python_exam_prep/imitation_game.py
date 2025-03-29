encrypted_message = input()

while True:
    command = input()
    if command == "Decode":
        break

    parts = command.split('|')
    action = parts[0]

    if action == "Move":
        number_of_letters = int(parts[1])
        encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]

    elif action == "Insert":
        index = int(parts[1])
        value = parts[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]

    elif action == "ChangeAll":
        substring = parts[1]
        replacement = parts[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

print(f"The decrypted message is: {encrypted_message}")