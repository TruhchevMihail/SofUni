numbers = input().split(", ")
beggars_count = int(input())

numbers = [int(num) for num in numbers]


sums = [0] * beggars_count


for i in range(len(numbers)):
    sums[i % beggars_count] += numbers[i]

print(sums)

