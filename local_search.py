from board import *
import random

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
		score += list_unique_elements(l)

	for col in range(dimension):
		l = []
		for row in range(dimension):
			l.append(board[row][col])
		score += list_unique_elements(l)
	return score

if __name__ == '__main__':
	board = easy_boards[0]
	print_board(board)
	d = init_board_to_dict(board)
	random_populate(board)
	print "============================================="
	print_board(board)

	print get_score(board)

