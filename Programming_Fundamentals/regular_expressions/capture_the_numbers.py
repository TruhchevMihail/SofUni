import re

line = input()
while line:
    regex = r"\d+"
    matches = re.findall(regex, line)
    if matches:
        print(" ".join(matches), end= " ")
    line = input()