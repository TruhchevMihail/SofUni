def sum_numbers(a, b):
    return a + b

def subtract(a, b):
    return a - b

def add_and_substract(a, b, c):
    result = sum_numbers(a, b)
    return subtract(result, c)

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(add_and_substract(number_1, number_2, number_3))
