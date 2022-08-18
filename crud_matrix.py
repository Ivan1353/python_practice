matrix = []

for row in range (6):
    matrix.append([x for x in input().split(" ")])

first_position = input()
my_row, my_col = int(first_position[1]), int(first_position[4])
while True:
    command_lst = input().split(", ")
    command = command_lst[0]
    if command == "Stop":
        break
    direction = command_lst[1]
    if len(command_lst) == 3:
        value = command_lst[2]

    if direction == "up":
        my_row -= 1
    elif direction == "down":
        my_row += 1
    elif direction == "left":
        my_col -= 1
    elif direction == "right":
        my_col += 1


    if command == "Create":
        if matrix[my_row][my_col] == ".":
            matrix[my_row][my_col] = value
    elif command ==  "Update":
        if matrix[my_row][my_col] != ".":
            matrix[my_row][my_col] = value
    elif command == "Delete":
        if matrix[my_row][my_col] != ".":
            matrix[my_row][my_col] = "."
    elif command == "Read":
        if matrix[my_row][my_col] != ".":
            print(matrix[my_row][my_col])


for line in matrix:
    print(" ".join(line))