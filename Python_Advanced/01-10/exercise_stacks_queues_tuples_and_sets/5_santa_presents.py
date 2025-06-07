from collections import deque


materials = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())

toys_magic = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

crafted_toys = {}
while materials and magic_level:
    material = materials[-1]
    magic = magic_level[0]

    if material == 0 and magic == 0:
        materials.pop()
        magic_level.popleft()
        continue
    if material == 0:
        materials.pop()
        continue
    if magic == 0:
        magic_level.popleft()
        continue

    result = material * magic

    if result in toys_magic:
        toy = toys_magic[result]
        crafted_toys[toy] = crafted_toys.get(toy, 0) + 1
        materials.pop()
        magic_level.popleft()

    elif result < 0:
        materials.pop()
        magic_level.popleft()
        materials.append(material + magic)
    else:
        magic_level.popleft()
        materials[-1] += 15        

success = ("Doll" in crafted_toys and "Wooden train" in crafted_toys) or \
         ("Teddy bear" in crafted_toys and "Bicycle" in crafted_toys)

if success:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print("Materials left: " + ", ".join(str(x) for x in reversed(materials)))

if magic_level:
    print("Magic left: " + ", ".join(str(x) for x in (magic_level)))

for toy, count in sorted(crafted_toys.items()):
    print(f"{toy}: {count}")
       