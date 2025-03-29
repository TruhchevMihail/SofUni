stock = {}
total_sold = 0

while True:
    command = input()
    if command == "Complete":
        break

    parts = command.split()
    action = parts[0]
    quantity = int(parts[1])
    food = parts[2]

    if action == "Receive":
        if quantity > 0:
            if food not in stock:
                stock[food] = 0
            stock[food] += quantity

    elif action == "Sell":
        if food not in stock:
            print(f"You do not have any {food}.")
        else:
            if stock[food] < quantity:
                sold_quantity = stock[food]
                print(f"There aren't enough {food}. You sold the last {sold_quantity} of them.")
                total_sold += sold_quantity
                del stock[food]
            else:
                stock[food] -= quantity
                print(f"You sold {quantity} {food}.")
                total_sold += quantity
                if stock[food] == 0:
                    del stock[food]

for food, quantity in stock.items():
    print(f"{food}: {quantity}")
print(f"All sold: {total_sold} goods")