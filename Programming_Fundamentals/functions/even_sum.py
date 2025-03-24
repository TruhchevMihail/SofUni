def is_even(number):
    return number % 2 == 0

def main():
    numbers = input().split()
    numbers = map(int, numbers)
    even_numbers = list(filter(is_even, numbers))
    print(even_numbers)

if __name__ == "__main__":
    main()
    