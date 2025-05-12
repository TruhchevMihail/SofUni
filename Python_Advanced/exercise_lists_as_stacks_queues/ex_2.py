stack = []

n = int(input())

for _ in range(n):
    query = input().split()
    command = query[0]

    if command == '1':
        number = int(query[1])
        stack.append(number)

    elif command == '2':
        stack.pop()

    elif command == '3':
        print(max(stack))
    
    elif command == '4':
        print(min(stack))

print(', '.join(map(str, stack)))