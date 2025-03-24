numbers = input().split()
numbers_to_remove = int(input())
numbers = [int(num) for num in numbers]

for _ in range(numbers_to_remove):
    numbers.remove(min(numbers))

print(", ".join(map(str, numbers)))
