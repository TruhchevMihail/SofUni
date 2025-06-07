n = int(input())
unique_elements = set()

for _ in range(n):
    compounds = input().split()
    unique_elements.update(compounds)

for element in unique_elements:
    print(element)