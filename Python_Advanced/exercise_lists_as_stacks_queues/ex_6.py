parentheses = input()

steck = []

for i in range(len(parentheses)):
    if parentheses[i] == "(" or parentheses[i] == "[" or parentheses[i] == "{":
        steck.append(parentheses[i])
    
    elif parentheses[i] == ")":
        if steck[-1] == "(":
            steck.pop()
    elif parentheses[i] == "]":
        if steck[-1] == "[":
            steck.pop()
    elif parentheses[i] == "}":
        if steck[-1] == "{":
            steck.pop()

    else:
        print("NO")
        break

else:
    if len(steck) == 0:
        print("YES")
    else:
        print("NO")