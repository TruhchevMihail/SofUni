usernames = input().split(', ')

for username in usernames:
    if 3 <= len(username) <= 16 and all(char.isalnum() or char == '-' or char == '_' for char in username):
        print(username)
