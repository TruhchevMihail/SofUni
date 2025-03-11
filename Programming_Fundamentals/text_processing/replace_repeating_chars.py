def compress_string(input_string):
    if not input_string:
        return input_string

    compressed = [input_string[0]]

    for i in range(1, len(input_string)):
        if input_string[i] != input_string[i - 1]:
            compressed.append(input_string[i])

    return ''.join(compressed)


input_string = input()
print(compress_string(input_string))
