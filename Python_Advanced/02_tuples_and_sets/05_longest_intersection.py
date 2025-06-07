n = int(input())
longest_intersection = set()

for _ in range(n):
    ranges = input().split('-')
    first_start, first_end = map(int, ranges[0].split(','))
    second_start, second_end = map(int, ranges[1].split(','))

    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_end + 1))

    intersection = first_set & second_set

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is [{', '.join(str(x) for x in sorted(longest_intersection))}] with length {len(longest_intersection)}")