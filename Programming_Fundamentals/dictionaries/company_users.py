companies = {}

while True:
    input_data = input()
    if input_data == "End":
        break

    company_name, id = input_data.split(" -> ")

    if company_name not in companies:
        companies[company_name] = []
    if id not in companies[company_name]:
        companies[company_name].append(id)

for company_name, id in companies.items():
    print(company_name)
    for i in id:
        print(f"-- {i}")