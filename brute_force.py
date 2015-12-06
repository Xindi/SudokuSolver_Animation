
def brute_force(board):
    dimension = len(board)
    for row in range(0, dimension):
        for col in range(0, dimension):
            if board[row][col] == '.':
                for i in range(1, dimension+1):
                    board[row][col] = str(i)
                    if board_is_valid( board, row, col ) and brute_force( board ):
                        return True
                    board[row][col] = '.'
                return False
    return True

def board_is_valid(board, row, col):
    # check row
    for i in range(0, 9):
        if i != col and board[row][i] == board[row][col]:
            return False

    # check column
    for j in range(0, 9):
        if j != row and board[j][col] == board[row][col]:
            return False

    # check square
    rSquare = row / 3
    cSquare = col / 3
    for i in range(rSquare*3, rSquare*3+3):
        for j in range(cSquare*3, cSquare*3+3):
            if not (i == row and j == col) and board[i][j] == board[row][col]:
                return False
    return True








