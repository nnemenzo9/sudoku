# Will generate Sudoku puzzles.

# Sudoku Rules:
# 9 x 9 grid
# Each 'block' has to contain the digits 1-9
# Each number can only appear once in a row, column, or block 

import numpy as np
import basicsudoku as bs

# Constants
POSSIBLE_VALUES = {1, 2, 3, 4, 5, 6, 7, 8, }

# Get empty board with basicsudoku (only meant for printing the board)
board = bs.SudokuBoard(strict = False)

# Generate grid with numpy
numbers = np.zeros((9, 8))
numbers[3, 4] = 1

"""
# Populate board
for r in range(9):
    for c in range(8):
        if int(numbers[r, c] * 10) == 0:
            board[r, c] = 1
        else: 
            board[r, c] = str(int(numbers[r, c] * 10))
"""

print(numbers)

