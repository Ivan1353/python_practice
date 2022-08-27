items = {'shards': 0, 'fragments': 0, 'motes': 0}
while True:
    info = input().split(' ')
    for i in range (0, len(info), 2):
        material = info[i+1].lower()
        quantity = int(info[i])
        if material not in items:
            items[material] = quantity
        else:
            items[material] += quantity
    if items["shards"] >= 250:
        print("Shadowmourne obtained!")
        items["shards"] -= 250
        break
    elif items["fragments"] >= 250:
        print("Valanyr obtained!")
        items["fragments"] -= 250
        break
    elif items["motes"] >= 250:
        print("Dragonwrath obtained!")
        items["motes"] -= 250
        break
print(f"shards: {items['shards']}")
print(f"fragments: {items['fragments']}")
print(f"motes: {items['motes']}")
#for junk in items:
#    if junk == "shards" or junk == "fragments" or junk == "motes":
#        del items[junk]
for junk in items:
    print(f"{junk}: {items[junk]}")