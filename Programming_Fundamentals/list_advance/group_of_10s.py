def group_numbers(sequence):
    numbers = [int(num.strip()) for num in sequence.split(",")]
    max_number = max(numbers)
    
    if max_number % 10 == 0:
        max_group = max_number
    else:
        max_group = ((max_number // 10) + 1) * 10
    
    group = 10
    while group <= max_group:
        current_group = [num for num in numbers if group - 10 < num <= group]
        print(f"Group of {group}'s: {current_group}")
        group += 10

sequence = input()
group_numbers(sequence)
