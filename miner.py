mine = dict()
counter = 0
while True:
    counter += 1
    word = input()
    if word == "stop":
        break
    if counter % 2 == 1:
        resource = word
        continue
    else:
        quantity = int(word)

    if resource in mine:
        mine[resource] = quantity
    else:
        mine[resource] += quantity

for thing in mine:
    print(f"{thing} -> {mine[thing]}")