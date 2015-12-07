from board import *
import random
from math import exp
from copy import deepcopy

''' convert the initial board state to a dictionary 
    for easy lookup later '''
def init_board_to_dict(init_board):
    result = set()
    dimension = len(init_board)
    for row in range(0, dimension):
        for col in range(0, dimension):
            if init_board[row][col] != ".":
                result.add( tuple((row, col)) )
    return result

''' checks whether the (row,col) is polulated in the initial 
    state '''
def is_init_populated(init_dict, row, col):
    return tuple((row,col)) in init_dict

def random_populate(board):
    rSquares = len(board) / 3
    cSquares = len(board) / 3
    for i in range(0, rSquares):
        for j in range(0, cSquares):
            random_subsquare(board, 3*i, 3*j)

''' helper for random_populate '''
def random_subsquare(board, row, col):
    avail = ["1","2","3","4","5","6","7","8","9"]
    for i in range(0, 3):
        r = row + i
        for j in range(0, 3):
            c = col + j
            if board[r][c] != ".":
                avail.remove(board[r][c])

    for i in range(0, 3):
        r = row + i
        for j in range(0, 3):
            c = col + j
            if board[r][c] == ".":
                pick = random.choice(avail)
                board[r][c] = pick
                avail.remove(pick)

''' count number of unique elements in a list
    example: [1,1,3,4] will return 2 '''
def list_unique_elements(l):
    dic = {}
    dimension = len(l)
    for i in range(dimension):
        val = l[i]
        if val in dic:
            dic[val] += 1
        else:
            dic[val] = 1
    
    count = 0
    for k, v in dic.iteritems():
        if v == 1:
            count += 1
    return count

def get_score(board):
    dimension = len(board)
    score = 0
    for row in range(dimension):
        l = board[row]
        score -= list_unique_elements(l)

    for col in range(dimension):
        l = []
        for row in range(dimension):
            l.append(board[row][col])
        score -= list_unique_elements(l)
    return score

def acceptance_prob(energy, new_energy, temperature):
    if new_energy < energy:
        return 1.0
    return exp( float(energy - new_energy) / temperature )

def get_new_state(board, init_dict):
    new_board = deepcopy(board)
    dim = len(board)
    square = random.randint(0,8)
    lower = square * dim
    upper = (square + 1) * dim - 1
    print "lower"
    print lower
    print "upper"
    print upper

    rand_pos1 = random.randint(lower, upper)
    rowcol1 = divmod(rand_pos1, dim)
    while is_init_populated(init_dict, rowcol1[0], rowcol1[1]):
        rand_pos1 = random.randint(lower, upper)
        rowcol1 = divmod(rand_pos1, dim)
    print "row col 1"
    print rand_pos1

    rand_pos2 = random.randint(lower, upper)
    rowcol2 = divmod(rand_pos2, dim)
    while rand_pos2 == rand_pos1 or is_init_populated(init_dict, rowcol2[0], rowcol2[1]):
        rand_pos2 = random.randint(lower, upper)
        rowcol2 = divmod(rand_pos2, dim)
    print "row col 2"
    print rand_pos2

    temp = new_board[rowcol1[0]][rowcol1[1]]
    new_board[rowcol1[0]][rowcol1[1]] = new_board[rowcol2[0]][rowcol2[1]]
    new_board[rowcol2[0]][rowcol2[1]] = temp

    #print_board(new_board)
    return new_board

def simulated_annealing(board):
    dim = len(board)
    init_dict = init_board_to_dict(board)

    cur_board = deepcopy(board)
    random_populate(cur_board)
    best_state = deepcopy(cur_board)

    cur_score = get_score(cur_board)
    best_score = cur_score
    count = 0

    cooling_rate = 0.00001
    T = 0.5
    while count < 400000:
        print T
        new_board = get_new_state(cur_board, init_dict)
        new_score = get_score(new_board)
        print new_score

        if (acceptance_prob(cur_score, new_score, T) > random.random()):
            cur_board = new_board
            cur_score = new_score
        
        if cur_score < best_score:
            best_state = deepcopy(cur_board)
            best_score = cur_score

        if cur_score == -2*dim*dim:
            cur_board = new_board
            break

        count += 1
        T = T * (1-cooling_rate)

    return best_state if best_score == -2*dim*dim else None


if __name__ == '__main__':
    board = easy_boards[0]
    print_board(board)
    result = simulated_annealing(board) 
    print_board(result)

