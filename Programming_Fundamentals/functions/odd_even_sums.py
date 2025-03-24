def sum_odd_even_digits(number):
    odd_sum = 0
    even_sum = 0

    for digit in str(number):
        digit = int(digit)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"

number = int(input())
result = sum_odd_even_digits(number)
print(result)