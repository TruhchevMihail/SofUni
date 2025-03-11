country_names = input().split(", ")
capital_cities = input().split(", ")
country_capital_dict = {country: capital for country, capital in zip(country_names, capital_cities)}

for country, capital in country_capital_dict.items():
    print(f"{country} -> {capital}")
