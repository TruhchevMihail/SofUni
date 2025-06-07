import string

with open("text.txt", "r") as file:
    lines = file.readlines()

with open("output.txt", "w") as file:
    for i, line in enumerate(lines, 1):
        stripped = line.rstrip('\n')
        letter_count = 0
        punctuation_count = 0
        for char in stripped:
            if char.isalpha():
                letter_count += 1
            elif char in string.punctuation:
                punctuation_count += 1
        file.write(f"Line {i}: {stripped} ({letter_count})({punctuation_count})\n")