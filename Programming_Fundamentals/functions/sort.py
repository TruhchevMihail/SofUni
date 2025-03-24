def sorted_list(list):
    return sorted(list)

def main():
    numbers = input().split() 
    numbers = list(map(int, numbers))
    sorted_numbers = sorted_list(numbers)
    print(sorted_numbers)

if __name__ == "__main__":
    main()
