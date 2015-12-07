from board import *
from brute_force import *
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

def random_populate(board, s_dim):
    rSquares = len(board) / s_dim
    cSquares = len(board) / s_dim
    for i in range(0, rSquares):
        for j in range(0, cSquares):
            random_subsquare(board, s_dim*i, s_dim*j, s_dim)

''' helper for random_populate '''
def random_subsquare(board, row, col, s_dim):
    small_avail = ["1","2","3","4","5","6","7","8","9"]
    large_avail = ["1","2","3","4","5","6","7","8","9", "10",
                   "11","12","13","14","15","16"]
    avail = small_avail if s_dim == 3 else large_avail
    for i in range(0, s_dim):
        r = row + i
        for j in range(0, s_dim):
            c = col + j
            if board[r][c] != ".":
                avail.remove(board[r][c])

    for i in range(0, s_dim):
        r = row + i
        for j in range(0, s_dim):
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

''' returns the score of current board state '''
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

''' calculates the probability of accepting the new state '''
def acceptance_prob(energy, new_energy, temperature):
    if new_energy < energy:
        return 1.0
    return exp( float(energy - new_energy) / temperature )

''' get the coordinates of the n-th subsquare '''
def get_square_pos(board, n, s_dim, init_dict):
    result = []
    rStart = (n / s_dim) * s_dim
    cStart = (n % s_dim) * s_dim
    for row in range(rStart, rStart+s_dim):
        for col in range(cStart, cStart+s_dim):
            if not is_init_populated(init_dict, row, col):
                result.append(tuple((row, col)))
    return result

''' randomly picks a subsquare and picks two positions within 
the subsquare that were not originally populated in the initial
state, and swap the values of the two positions ''' 
def get_new_state(board, init_dict, s_dim):
    new_board = deepcopy(board)
    dim = len(board)
    square = random.randint(0,dim-1)

    square_pos = get_square_pos(board, square, s_dim, init_dict)
    (rowcol1, rowcol2) = random.sample(square_pos, 2)

    temp = new_board[rowcol1[0]][rowcol1[1]]
    new_board[rowcol1[0]][rowcol1[1]] = new_board[rowcol2[0]][rowcol2[1]]
    new_board[rowcol2[0]][rowcol2[1]] = temp

    return new_board

def simulated_annealing(board, s_dim, states):
    dim = len(board)
    init_dict = init_board_to_dict(board)

    cur_board = deepcopy(board)
    random_populate(cur_board, s_dim)
    best_state = deepcopy(cur_board)

    cur_score = get_score(cur_board)
    best_score = cur_score
    count = 0

    cooling_rate = 0.00001
    T = 0.4
    while count < 400000:
        new_board = get_new_state(cur_board, init_dict, s_dim)
        new_score = get_score(new_board)

        if (acceptance_prob(cur_score, new_score, T) > random.random()):
            cur_board = new_board
            cur_score = new_score
            states.append( deepcopy(new_board) )
        
        if cur_score < best_score:
            best_state = deepcopy(cur_board)
            best_score = cur_score

        if new_score == -2*dim*dim:
            cur_board = new_board
            break

        count += 1
        T = T * (1-cooling_rate)

    return best_state if best_score == -2*dim*dim else None

if __name__ == '__main__':
    board = easy_boards[0]
    print_board(board)
    init_dict = init_board_to_dict(board)
    states = []
    result = simulated_annealing(board, 3, states)
    print_board(result)
    
