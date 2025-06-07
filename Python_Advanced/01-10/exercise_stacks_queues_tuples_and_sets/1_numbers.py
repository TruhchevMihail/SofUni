first_sequences = set([int(x) for x in input().split()])
second_sequences = set([int(x) for x in input().split()])

for _ in range(int(input())):
    operration = input().split()

    action = operration[0] + " " + operration[1]
    inputs = operration[2:]

    if action == "Add First":
        first_sequences.update(int(x) for x in inputs)
    
    if action == "Add Second":
        second_sequences.update(int(x) for x in inputs)
    
    if action == "Remove First":
        first_sequences.difference_update(int(x) for x in inputs)
    
    if action == "Remove Second":
        second_sequences.difference_update(int(x) for x in inputs)
    
    if action == "Check Subset":
        if first_sequences.issubset(second_sequences) or second_sequences.issubset(first_sequences):
            print("True")
        else:
            print("False")

print(", ".join(str(x) for x in sorted(first_sequences)))
print(", ".join(str(x) for x in sorted(second_sequences)))          