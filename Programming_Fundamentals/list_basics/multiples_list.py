factor = int(input())
counts = int(input())
multiples_list = [] 

for count in range(1, counts + 1):
    multiples_list.append(factor * count)
    
print(multiples_list)
