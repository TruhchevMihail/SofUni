stack = []

n = int(input())

for _ in range(n):
    query = input().split()
    command = query[0]

    if command == '1':
        number = int(query[1])
        stack.append(number)

    elif command == '2' and stack:
        stack.pop()

    elif command == '3' and stack:
        print(max(stack))

    elif command == '4' and stack:
        print(min(stack))

print(', '.join(map(str, reversed(stack))))