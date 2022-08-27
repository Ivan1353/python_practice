force_dict = dict()
condition = False
while True:
    info = input()
    if info == "Lumpawaroo":
        break
    else:
        if "|" in info:
            info = info.split(" | ")
            side = info[0]
            person = info[1]
            if side not in force_dict:
                force_dict[side] = list()
            for strana in force_dict:
                if person in force_dict[strana]:
                    condition = True
            if condition == False:
                force_dict[side].append(person)
            condition = False

        elif "->" in info:
            info = info.split(" -> ")
            person = info[0]
            side = info[1]
            if side not in force_dict:
                force_dict[side] = list()
            else:
                for strana in force_dict:
                    if person in force_dict[strana]:
                        force_dict[strana].remove(person)
                force_dict[side].append(person)
                print(f"{person} joins the {side} side!")

for strana in force_dict:
    if len(force_dict[strana]) != 0:
        print(f"Side: {strana}, Members: {len(force_dict[strana])}")
        force_list = ["! "+ string for string in force_dict[strana]]
        spisuk = "\n".join(force_list)
        print(spisuk)