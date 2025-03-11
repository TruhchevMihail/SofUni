phonebook = {}

while True:
    entry = input()
    if entry.isdigit():
        times = int(entry)
        break
    name, number = entry.split("-")
    phonebook[name] = number

for _ in range(times):
    searched_name = input()
    if searched_name in phonebook:
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
