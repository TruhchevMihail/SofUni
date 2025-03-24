def minimum_number(numbers):
    return min(numbers)

def maximum_number(numbers):
    return max(numbers)

def sum_numbers(numbers):
    return sum(numbers)

numbers = input().split()
numbers = (list(map(int, numbers)))

print(f"The minimum number is {minimum_number(numbers)}")
print(f"The maximum number is {maximum_number(numbers)}")
print(f"The sum number is: {sum_numbers(numbers)}")
