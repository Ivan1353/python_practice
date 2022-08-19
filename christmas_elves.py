from collections import deque

dwarfs_energy = deque([int(x) for x in input().split()])
boxes = deque([int(x) for x in input().split()])

energy_used = 0
total_toys = 0
counter = 0

while True:
    counter += 1
    dwarf = dwarfs_energy[0]
    energy_needed = boxes[-1]
    if counter%3 == 0:
        energy_needed *= 2
    if dwarf >= energy_needed:
        energy_used += energy_needed
        dwarfs_energy[0] -= energy_needed-1
        boxes.pop()

        if counter % 5 == 0:
            dwarfs_energy[0] += 1
            continue
        elif counter % 3 == 0:
            dwarfs_energy[0] -= energy_needed
            total_toys += 1

        total_toys += 1

    else:
        dwarfs_energy[0] *= 2

    dwarfs_energy.append(dwarfs_energy.popleft())

    if len(boxes) == 0:
        break
    print(f"Toys: {total_toys}")
    print(f"Energy: {energy_used}")
    print(f"Elves left: {','.join([str(x) for x in dwarfs_energy])}")
    print(f"boxes:{boxes}")
    print(f"{energy_needed}")

print(f"Toys: {total_toys}")
print(f"Energy: {energy_used}")
print(f"Elves left: {','.join([str(x) for x in dwarfs_energy])}")