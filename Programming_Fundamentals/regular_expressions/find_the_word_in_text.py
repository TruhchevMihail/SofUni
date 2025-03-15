import re

text = input()
word = input()

regex = fr'\b{word}\b'
matches = re.findall(regex, text, re.IGNORECASE)

print(len(matches))