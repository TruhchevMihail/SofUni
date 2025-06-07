n = int(input())

unique_usernames = set()

for name in range(n):
    username = input()
    unique_usernames.add(username)

print(*unique_usernames, sep='\n')