numbers = input().split()
counts = {}

for num in numbers:
    num_f = float(num)
    if num_f not in counts:
        counts[num_f] = 0
    counts[num_f] += 1

for num, count in counts.items():
    print(f"{num:.1f} - {count} times")