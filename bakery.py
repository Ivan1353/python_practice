data = input().split(' ')
bakery = dict()

for i in range (0, len(data), 2):
    food = data[i]
    quant = int(data[i+1])
    bakery[food] = quant

print(bakery)