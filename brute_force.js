"use strict";
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
];

var brute_force = function(board) {
    var dimension = board.length;
    for (var row = 0; row < dimension; row++) { 
    	for (var col = 0; col < dimension; col++) {
    		if (board[row][col] == ".") {
    			for (var i = 1; i < dimension+1; i++) {
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
};

function board_is_valid(board, row, col) {
	var dimension = board.length;
	// check row
	for (var iii = 0; iii < dimension; iii++) {
		if( iii != col && board[row][iii] == board[row][col] ) {
			return false;
		}
	}

	// check column
	for (var j = 0; j < dimension; j++) {
		if( j != row && board[j][col] == board[row][col]) {
			return false;
		}
	}

	// check square
	var rSquare = row / 3;
	var cSquare = col / 3;
	for (var ii = rSquare*3; ii < rSquare*3+3; ii++) {
		for (var jj = cSquare*3; jj < cSquare*3+3; jj++) {
			if( !(ii == row && jj == col) && (board[ii][jj] == board[row][col]) ) {
				return false;
			}
		}
	}
	return true;
}