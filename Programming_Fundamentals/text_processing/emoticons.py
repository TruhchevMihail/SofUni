text = input()

emoticons = []

for i in range(len(text) - 1):
    if text[i] == ":" and text[i + 1] != " ":
        emoticons.append(text[i:i+2])

for emoticon in emoticons:
    print(emoticon)
