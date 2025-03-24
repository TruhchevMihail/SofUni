def is_palindrome(number):
    return str(number) == str(number)[::-1]

def check_palindromes(numbers):
    results = []
    for number in numbers:
        results.append(is_palindrome(number))
    return results

def main():
    input_numbers = input()
    numbers = [int(num) for num in input_numbers.split(", ")]
    results = check_palindromes(numbers)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()