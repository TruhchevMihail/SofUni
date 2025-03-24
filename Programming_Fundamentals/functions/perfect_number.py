def is_perfect_number(n):
    if n < 1:
        return "It's not so perfect."
    
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    
    if divisors_sum == n:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

number = int(input())
print(is_perfect_number(number))
