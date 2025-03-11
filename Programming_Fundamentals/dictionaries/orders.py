products = {}

while True:
    input_line = input()

    if input_line == "buy":
        break

    name, price, quantity = input_line.split()
    price = float(price)
    quantity = int(quantity)

    if name in products:
        products[name]["quantity"] += quantity
        products[name]["price"] = price
    else:
        products[name] = {"price": price, "quantity": quantity}

for name, item in products.items():
    total_price = item["price"] * item["quantity"]
    print(f"{name} -> {total_price:.2f}")
