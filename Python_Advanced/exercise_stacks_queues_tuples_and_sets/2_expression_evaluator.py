from math import floor

expression = input().split()
numbers = []

operators = {
    '+': lambda nums: sum(nums),
    '-': lambda nums: nums[0] - sum(nums[1:]),
    '*': lambda nums: eval('*'.join(map(str, nums))),
    '/': lambda nums: floor(nums[0] / eval('*'.join(map(str, nums[1:])))) if len(nums) > 1 else nums[0]
}

i = 0
while i < len(expression):
    token = expression[i]
    if token.lstrip('-').isdigit():
        numbers.append(int(token))
    else:
        result = None
        if token == '+':
            result = operators['+'](numbers)
        elif token == '-':
            result = operators['-'](numbers)
        elif token == '*':
            result = numbers[0]
            for n in numbers[1:]:
                result *= n
        elif token == '/':
            result = numbers[0]
            for n in numbers[1:]:
                result = floor(result / n)
        if result is not None:
            numbers = [result]
    i += 1

print(numbers[0])