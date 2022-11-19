def check_soduku(row, column, number, matrix_board):
    check = 0
    for i in range(0, 9):
        if matrix_board[row][i] == number:
            check = 1
    for i in range(0, 9):
        if matrix_board[i][column] == number:
            check = 1
    row = row-row % 3
    column = column-column % 3

    for i in range(0, 3):
        for j in range(0, 3):
            if matrix_board[row+i][column+j] == number:
                check = 1
    if check == 1:
        return False
    else:
        return True


def sudoku_solver(matrix):
    break_condition = 0
    for i in range(0, 9):
        for j in range(0, 9):
            if matrix[i][j] == 0:
                break_condition = 1
                row = i
                column = j
                break

    if break_condition == 0:
        return True

    for i in range(0, 10):
        if check_soduku(row, column, i, matrix):
            matrix[row][column] = i
            if sudoku_solver(matrix):
                return True
            matrix[row][column] = 0
    return False
