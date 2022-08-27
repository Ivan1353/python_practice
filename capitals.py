countries = input().split(", ")
capitals = input().split(", ")
dictio = dict(zip(countries, capitals))
for country in dictio:
    print(f"{country} -> {dictio[country]}")