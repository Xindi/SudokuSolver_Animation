from board import *
from brute_force import *

if __name__ == '__main__':
    easy_board = get_easy_board()
    print "=========== before =========="
    print_board(easy_board)
    brute_force(easy_board)
    print "=========== after ==========="
    print_board(easy_board)