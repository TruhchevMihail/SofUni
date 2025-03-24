first_sequence = input().split(", ")
second_sequence = input().split(", ")

result = [substring for substring in first_sequence if any(substring in string for string in second_sequence)]


print(result)