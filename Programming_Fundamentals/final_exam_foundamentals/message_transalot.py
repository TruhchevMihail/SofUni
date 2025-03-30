import re

n = int(input())
pattern = r"^!(?P<command>[A-Z][a-z]{2,})!:\[(?P<text>[A-Za-z]{8,})\]$"

for _ in range(n):
    message = input()

    match = re.match(pattern, message)


    if match:
        command = match.group("command")
        text = match.group("text")

        ascii_values = [str(ord(char)) for char in text]
        print(f"{command}: {' '.join(ascii_values)}")

    else:
        print("The message is invalid")
        