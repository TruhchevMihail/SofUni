n, m = map(int, input().split())

set_n = set()
set_m = set()

for _ in range(n):
    set_n.add(input())

for _ in range(m):
    set_m.add(input())

common_elements = set_n & set_m

for element in common_elements:
    print(element)