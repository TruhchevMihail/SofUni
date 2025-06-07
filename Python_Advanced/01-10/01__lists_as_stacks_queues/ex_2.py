expression = input()

sets = []

for index in range(len(expression)):
    if expression[index] == '(':
        sets.append(index)
    elif expression[index] == ')':
        if len(sets) > 0:
            start_index = sets.pop()
            print(expression[start_index:index + 1])