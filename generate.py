import itertools
import random
from board import *

def attempt_board(m=3):
    """Make one attempt to generate a filled m**2 x m**2 Sudoku board,
    returning the board if successful, or None if not.

    """
    n = m**2
    numbers = list(range(1, n + 1))
    board = [[None for _ in range(n)] for _ in range(n)]
    for i, j in itertools.product(range(n), repeat=2):
        i0, j0 = i - i % m, j - j % m # origin of mxm block
        random.shuffle(numbers)
        for x in numbers:
            if (x not in board[i]                     # row
                and all(row[j] != x for row in board) # column
                and all(x not in row[j0:j0+m]         # block
                        for row in board[i0:i])):
                board[i][j] = x
                break
        else:
            # No number is valid in this cell.
            return None
    return board

if __name__ == '__main__':
    board = attempt_board(m=3)
    print_board(board)