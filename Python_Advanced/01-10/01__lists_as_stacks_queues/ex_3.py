queue = []

while True:
    client = input()
    
    if client == "End":
        print(f"{len(queue)} people remaining.")
        break
    elif client == "Paid":
        while queue:
            print(queue.pop(0))
    else:
        queue.append(client)