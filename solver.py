# Will solve Sudoku puzzles and be used in Sudoku puzzle generation.

# Board is modeled as 2D numpy array
import numpy as np
import basicsudoku as bs

# Constants
POSSIBLE_VALUES = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Numpy array will be filled with values hand (until another method can be found)
# Basicsudoku is for printing the board, we can use a loop to fill the board with numpy values.
grid = np.zeros((9, 9), dtype = int)

"""
Basic algorithm:

Iterate through entire board (81 cells) 
    For each cell, generate possible candidate values. 
        Place the first candidate value in the cell and move on to the next square.
            Generate possible candidate values for the next square
                If no possible value, backtrack to the value before and try next candidate value.
    Algorithm is complete when the entire board is finished. 
"""

# Board is a numpy array; solve() is only called one time
def solve(board):
    while not solved(board):
        

# Return true if no matching value found, false if matching value found
def checkColumn(board, c, value):
    for i in range(9):
        if value == board[i, c]:
            return false
    return true

# Return true if no matching value found, false if matching value found
def checkRow(board, r, value):
    for i in range(9):
        if value  == board[r, i]:
            return false
    return true

# Return true if no matching value found, false if matching value found
def checkSubgrid(board, c, r, value):
    # Get starting point. Ex: If [4, 4] then starting point is [3, 3]
    startingC = (c / 3) * 3
    startingR = (r / 3) * 3

    # Iterate through 9 cells in subgrid
    for r in range(3):
        for c in range(3):
            if board[startingR + r, startingC + c] == value:
                return false
    return true

# Check if the board is solved; return true of the board is solved correcly and false if not
def solved(board):
    for r in range(9):
        for c in range(9):
            value = board[r, c]

            # Check if the current value is valid
            if not checkRow(board, r, value) or not checkColumn(board,c , value) or not checkSubgrid(board, c, r, value):
                return false
    return true



