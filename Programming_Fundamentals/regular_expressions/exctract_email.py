import re

text = input()

regex = r'\s([a-z0-9]+[a-z0-9\.\-\_]*@([a-z\-]+)(\.[a-z]+)+)\b'

matches = re.findall(regex, text)
for match in matches:
    print(match[0])