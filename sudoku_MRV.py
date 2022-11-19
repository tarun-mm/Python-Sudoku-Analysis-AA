def check_soduku(row, col, num, sudoku):
    check = 0
    for i in range(0, 9):
        if sudoku[row][i] == num:
            check = 1
    for i in range(0, 9):
        if sudoku[i][col] == num:
            check = 1
    row = row-row % 3
    col = col-col % 3

    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku[row+i][col+j] == num:
                check = 1
    if check == 1:
        return False
    else:
        return True


def sudoku_solver(sudoku):
    break_condition = 0
    checking_range = []
    for i in range(0, 9):
        for j in range(0, 9):
            if sudoku[i][j] == 0:
                break_condition = 1
                temp = []
                temp.append([i, j])
                temp_2 = []
                for num in range(0, 10):
                    if check_soduku(i, j, num, sudoku):
                        temp_2.append(num)
                temp.append(len(temp_2))
                checking_range.append(temp)
    if break_condition == 0:
        return True

    minimum_range_selection = checking_range[0][0]

    low = checking_range[0][1]
    for i in range(0, len(checking_range)):
        if checking_range[i][1] < low:
            low = checking_range[i][1]
            minimum_range_selection = checking_range[i][0]
    row = minimum_range_selection[0]
    column = minimum_range_selection[1]

    for i in range(0, 10):
        if check_soduku(row, column, i, sudoku):
            sudoku[row][column] = i
            if sudoku_solver(sudoku):
                return True
            sudoku[row][column] = 0
    return False
