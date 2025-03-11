while True:
    name = input()
    if name == "Voldemort":
        print("You must not speak of that name!")
        break

    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break

    if len(name) == 5:
        print(f"{name} goes to Slytherin.")
        continue
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
        continue
    elif len(name) < 5:
        print(f"{name} goes to Gryffindor.")
        continue
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")
        continue

