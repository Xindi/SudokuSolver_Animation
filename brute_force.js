var easy_boards = [
    [   [".",".","6",".",".",".",".",".","."],
        ["8",".",".",".","7",".","1","3","5"],
        ["1","4",".","3","2",".",".","8","."],
        ["3",".",".","4",".","2","6","1","."],
        [".","1",".",".","6",".",".","2","."],
        [".","6","7","1",".","8",".",".","9"],
        [".","2",".",".","4","7",".","5","8"],
        ["4","7","9",".","8",".",".",".","1"],
        [".",".",".",".",".",".","9",".","."],
    ],
    [],
    []
]

function brute_force(board) {
    var dimension = board.length;
    for (row = 0; i < dimension; row++) { 
    	for (col = 0; col < dimension; col++) {
    		if (board[row][col] == ".") {
    			for (i = 1; i < dimension+1; i++) {
    				board[row][col] = i.toString();
    				if( board_is_valid(board, row, col) && brute_force(board)) {
    					return true;
    				}
    				board[row][col] = ".";
    			}
    			return false;
    		}
    	}
	}
	return true;
}

function board_is_valid(board, row, col) {
	var dimension = board.length;
	// check row
	for (i = 0; i < dimension; i++) {
		if( i != col && board[row][i] == board[row][col] ) {
			return false;
		}
	}

	// check column
	for (j = 0; j < dimension; j++) {
		if( j != row && board[j][col] == board[row][col]) {
			return false;
		}
	}

	// check square
	var rSquare = row / 3;
	var cSquare = col / 3;
	for (i = rSquare*3; i < rSquare*3+3; i++) {
		for (j = rSquare*3; j < rSquare*3+3; j++) {
			if( !(i == row && j == col) && (board[i][j] == board[row][col]) ) {
				return false;
			}
		}
	}
	return true;
}