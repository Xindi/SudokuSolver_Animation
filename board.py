''' This file represents the board of a sudoku puzzle, and includes functions
    that generates the initial game state.

    board is represented by a 2D list, where each element is the value at the
    corresponding index position. "." at any index position indicates that 
    position is empty.
'''
easy_boards = [
    [   ['.','.','6','.','.','.','.','.','.'],
        ['8','.','.','.','7','.','1','3','5'],
        ['1','4','.','3','2','.','.','8','.'],
        ['3','.','.','4','.','2','6','1','.'],
        ['.','1','.','.','6','.','.','2','.'],
        ['.','6','7','1','.','8','.','.','9'],
        ['.','2','.','.','4','7','.','5','8'],
        ['4','7','9','.','8','.','.','.','1'],
        ['.','.','.','.','.','.','9','.','.'],
    ],
    [],
    []
]

def print_board(board):
    dimension = len(board)
    for i in range(0, dimension):
        print board[i]

def get_easy_board():
    return easy_boards[0]
