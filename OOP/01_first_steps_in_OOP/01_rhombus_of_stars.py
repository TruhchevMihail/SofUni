def upper_part(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)


def lower_part(n):
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "* " * i)

def rhombus_of_stars(n):
    upper_part(n)
    lower_part(n)

rhombus_of_stars(int(input()))