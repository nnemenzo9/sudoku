# Will solve Sudoku puzzles and be used in Sudoku puzzle generation.

# Basic algorithm:
# For each cell, generate possible candidate values. 
# Go through each candidate value and try to solve the puzzle. 


# Board is modeled as 2D numpy array
import numpy as np
import basicsudoku as bs

# Constants
POSSIBLE_VALUES = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Numpy array will be filled with values using solving algorithm
# Basicsudoku is for printing the board, we can use a loop to fill the board with numpy values.
grid = np.zeros((9, 9), dtype = int)
print(grid)