number_of_pieces = int(input())
pieces = {}

for _ in range(number_of_pieces):
    piece_data = input().split('|')
    piece = piece_data[0]
    composer = piece_data[1]
    key = piece_data[2]
    pieces[piece] = [composer, key]

while True:
    command = input()
    if command == "Stop":
        break

    command_parts = command.split('|')
    action = command_parts[0]

    if action == "Add":
        piece = command_parts[1]
        composer = command_parts[2]
        key = command_parts[3]

        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif action == "Remove":
        piece = command_parts[1]
        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        piece = command_parts[1]
        new_key = command_parts[2]
        if piece in pieces:
            pieces[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, info in pieces.items():
    composer, key = info
    print(f"{piece} -> Composer: {composer}, Key: {key}")


