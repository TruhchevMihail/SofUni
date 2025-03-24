version = input().split(".")
version = [int(x) for x in version]
version[-1] += 1
for i in range(len(version) - 1, 0, -1):
    if version[i] == 10:
        version[i] = 0
        version[i - 1] += 1
print(".".join(str(x) for x in version))