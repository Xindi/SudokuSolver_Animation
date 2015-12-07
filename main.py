import sys
import numpy
from copy import deepcopy
from local_search import *
from brute_force import *

def read_boards(filename):
    count = 0
    with open(filename) as f:
        lines = f.readlines()
        boards = []
        board = []
        for line in lines:
            row = line.strip().split(" ")
            board.append(row)
            if count % 9 == 8:
                boards.append(deepcopy(board))
                board = []
            count += 1
    return boards

def run_brute_force(filename):
    boards = read_boards(filename)
    stats = []
    success = 0

    max_states = -1
    min_states = sys.maxint
    total_states = 0
    for board in boards:
        states = []
        r = brute_force(board, states)
        if r == True:
            cur_states = len(states)
            max_states = max(max_states, cur_states)
            min_states = min(min_states, cur_states)
            total_states += cur_states
            stats.append(cur_states)
            success += 1
    print "success " + str(success)
    result = {}
    result['max'] = max_states
    result['min'] = min_states
    result['total'] = total_states
    result['average'] = float(total_states) / 20
    result['median'] = numpy.median(stats)
    return result

def run_simulated_annealing(filename):
    boards = read_boards(filename)
    stats = []
    success = 0

    max_states = -1
    min_states = sys.maxint
    total_states = 0
    for board in boards:
        print "---------------------------------"
        print_board(board)
        states = []
        r = simulated_annealing(board, 3, states)
        while r == None:
            print "try again ~~~~~~~~~~~~~~"
            print_board(board)
            states = []
            r = simulated_annealing(board, 3, states)
        cur_states = len(states)
        max_states = max(max_states, cur_states)
        min_states = min(min_states, cur_states)
        total_states += cur_states
        stats.append(cur_states)
        success += 1
    print "success " + str(success)
    result = {}
    result['max'] = max_states
    result['min'] = min_states
    result['total'] = total_states
    result['average'] = float(total_states) / success
    result['median'] = numpy.median(stats)
    return result

if __name__ == '__main__':
    files = ['files/easy_puzzles.txt', 'files/medium_puzzles.txt', 'files/hard_puzzles.txt']
    # print " ---------- Brute force ----------"
    # for f in files:
    #     result = run_brute_force(f)
    #     print "======================="
    #     print f
    #     print "max " + str(result['max'])
    #     print "min " + str(result['min'])
    #     print "total " + str(result['total'])
    #     print "average " + str(result['average'])
    #     print "median " + str(result['median'])

    print " ------ Simulated Annealing ------"
    for f in files:
        result = run_simulated_annealing(f)
        print "======================="
        print f
        print "max " + str(result['max'])
        print "min " + str(result['min'])
        print "total " + str(result['total'])
        print "average " + str(result['average'])
        print "median " + str(result['median'])


    








