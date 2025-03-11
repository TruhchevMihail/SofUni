def process_explosions(input_string):
    result = []
    explosion_strength = 0
    index = 0

    while index < len(input_string):
        char = input_string[index]
        if char == '>':
            result.append(char)
            explosion_strength += int(input_string[index + 1])
        elif explosion_strength > 0:
            explosion_strength -= 1
        else:
            result.append(char)
        index += 1

    return ''.join(result)


input_string = input()
print(process_explosions(input_string))
