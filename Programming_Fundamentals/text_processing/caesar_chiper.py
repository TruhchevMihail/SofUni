text = input()

encrypted_text = "".join(chr(ord(char) + 3) for char in text)
print(encrypted_text)
