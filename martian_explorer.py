matrix = []
rover_pos, water_pos, metal_pos, concrete_pos, rock_pos = [], [], [], [], []
deposit_nums = 0
water_num, metal_num, concrete_num = 0, 0, 0

for ln in range (6):
    line = [x for x in input().split()]
    matrix.append(line)
    for rn in range(len(line)):
        if line[rn] == "E":
            rover_pos = [ln,rn]
        if line[rn] == "W":
            water_pos.append([ln,rn])
        if line[rn] == "M":
            metal_pos.append([ln, rn])
        if line[rn] == "C":
            concrete_pos.append([ln, rn])
        if line[rn] == "R":
            rock_pos.append([ln, rn])

commands = input().split(", ")

for command in commands:

    if command == "up":
        rover_pos[0] -= 1
    elif command == "down":
        rover_pos[0] += 1
    elif command == "left":
        rover_pos[1] -= 1
    elif command == "right":
        rover_pos[1] += 1

    for water in range(len(water_pos)):
        if water_pos[water] == rover_pos:
            water_num += 1
            print (f"Water deposit found at ({rover_pos[0]}, {rover_pos[1]})")
    for metal in range(len(metal_pos)):
        if metal_pos[metal] == rover_pos:
            metal_num += 1
            print (f"Metal deposit found at ({rover_pos[0]}, {rover_pos[1]})")
    for concrete in range(len(concrete_pos)):
        if concrete_pos[concrete] == rover_pos:
            concrete_num += 1
            print (f"Concrete deposit found at ({rover_pos[0]}, {rover_pos[1]})")
    for rock in range(len(rock_pos)):
        if rock_pos[rock] == rover_pos:
            print (f"Rover got broken at ({rover_pos[0]}, {rover_pos[1]})")
            break

if water_num>0 and metal_num>0 and concrete_num>0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")