import re

pattern = r">>(?P<furniture>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)"
furniture_list = []
total_money = 0.0

while True:
    line = input()
    if line == "Purchase":
        break

    match = re.search(pattern, line)
    if match:
        furniture = match.group("furniture")
        price = float(match.group("price"))
        quantity = int(match.group("quantity"))
        furniture_list.append(furniture)
        total_money += price * quantity

print("Bought furniture:")
for furniture in furniture_list:
    print(furniture)
print(f"Total money spend: {total_money:.2f}")
