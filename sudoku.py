def is_valid(board, row, col, num):
    # check the number in the row
    for x in range(9):
        if board[row][x] == num:
            return False

    # check the number in the column
    for x in range(9):
        if board[x][col] == num:
            return False

    # check the number in the current 3x3 box
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False
    return True

def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num  # try this number for the cell

                        if solve(board):  # continue with this number
                            return True

                        board[i][j] = 0  # remove the number as it leads to no solution
                return False  # trigger backtracking
    return True

# To use the function:

# The 0's in the grid represent empty values
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve(grid):
    for i in range(9):
        print(grid[i])
else:
    print("No solution exists")