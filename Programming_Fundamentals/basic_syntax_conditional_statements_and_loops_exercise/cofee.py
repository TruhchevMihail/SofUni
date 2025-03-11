coffees = 0

while True:
    commands= input().split()

    if "END" in commands:
        break

    for command in commands:
        if (command.lower() == "coding"
                or command.lower() == "dog"
                or command.lower() == "cat"
                or command.lower() == "movie"):
            if command.isupper():
                coffees += 2
            else:
                coffees += 1

if coffees <= 5:
    print(coffees)
else:
    print("You need extra sleep")