followers = {}

while True:
    command = input()
    if command == "Log out":
        break

    command_parts = command.split(": ")
    action = command_parts[0]

    if action == "New follower":
        username = command_parts[1]
        if username not in followers:
            followers[username] = {"likes": 0, "comments": 0}

    elif action == "Like":
        username, count = command_parts[1], int(command_parts[2])
        if username not in followers:
            followers[username] = {"likes": count, "comments": 0}
        else:
            followers[username]["likes"] += count

    elif action == "Comment":
        username = command_parts[1]
        if username not in followers:
            followers[username] = {"likes": 0, "comments": 1}
        else:
            followers[username]["comments"] += 1

    elif action == "Blocked":
        username = command_parts[1]
        if username in followers:
            del followers[username]
        else:
            print(f"{username} doesn't exist.")

print(f"{len(followers)} followers")

for username, stats in followers.items():
    end_status = stats["likes"] + stats["comments"]
    print(f"{username}: {end_status}")
