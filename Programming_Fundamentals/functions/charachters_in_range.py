def characters_in_range(char1, char2):
    start = min(ord(char1), ord(char2)) + 1
    end = max(ord(char1), ord(char2))
    result = ' '.join(chr(i) for i in range(start, end))
    return result

char1 = input()
char2 = input()
print(characters_in_range(char1, char2))
