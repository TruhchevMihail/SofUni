symbols = {"-", ",", ".", "!", "?"}

with open("text.txt") as file:
    for idx, line in enumerate(file):
        if idx % 2 == 0:
            line = line.strip()
            for symbol in symbols:
                line = line.replace(symbol, "@")
            words = line.split()
            reversed_words = words[::-1]
            print(" ".join(reversed_words))