import re

input_Line = input()
regex = r'\b_([A-Za-z0-9]+)\b'
matches = re.findall(regex, input_Line)
print(",".join(matches))