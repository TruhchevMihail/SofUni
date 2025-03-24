def positive_numbers(numbers):
    postivie_numbers = []
    for num in numbers:
        if int(num) >= 0:
            postivie_numbers.append(num)
    return postivie_numbers

def negative_numbers(numbers):
    negative_numbers = []
    for num in numbers:
        if int(num) < 0:
            negative_numbers.append(num)
    return negative_numbers

def even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if int(num) % 2 == 0:
            even_numbers.append(num)
    return even_numbers

def odd_numbers(numbers):
    odd_numbers = []
    for num in numbers:
        if int(num) % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers

numbers = input().split(", ")

print("Positive: " + ", ".join(positive_numbers(numbers)))
print("Negative: " + ", ".join(negative_numbers(numbers)))
print("Even: " + ", ".join(even_numbers(numbers)))
print("Odd: " + ", ".join(odd_numbers(numbers)))
