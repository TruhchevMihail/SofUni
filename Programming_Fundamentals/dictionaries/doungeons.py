key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
legendary_rewards = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
obtained_item = None

while True:
    tokens = input().split()
    for i in range(0, len(tokens), 2):
        quantity = int(tokens[i])
        material = tokens[i+1].lower()
        if material in key_materials:
            key_materials[material] += quantity
            if key_materials[material] >= 250 and obtained_item is None:
                obtained_item = legendary_rewards[material]
                key_materials[material] -= 250
                break
        else:
            if material not in junk:
                junk[material] = quantity
            else:
                junk[material] += quantity
    if obtained_item is not None:
        break

print(f"{obtained_item} obtained!")
for material in ["shards", "fragments", "motes"]:
    print(f"{material}: {key_materials[material]}")
for material, quantity in junk.items():
    print(f"{material}: {quantity}")
