# Contains puzzle generation functions (uses solving functions)

# TODO: Optimize grid generation

# Board is modeled as 2D numpy array
import random as r
import solving as s
import global_var

# Variation on solving algorithm to generate solution grid; needs empty input
def generate_grid(board):
    if not s.find_empty_cell(board):
        return True
    else: 
        coords = s.find_empty_cell(board)

    # Generate the possible values in a cell
    POSSIBLE_VALUES = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    # Pick a random value, if there are no values left to pick, backtrack
    while len(POSSIBLE_VALUES) > 0:
        
        # Generate a value and check if its in the set, if its in the set generate a new value
        value = r.randint(1, 10)
        
        if value in POSSIBLE_VALUES: 
            POSSIBLE_VALUES.remove(value)
        else:             
            while value not in POSSIBLE_VALUES:
                value = r.randint(1, 10)
                if value in POSSIBLE_VALUES:
                    POSSIBLE_VALUES.remove(value)
                    break
        
        if s.check_if_valid(board, coords, value):
            board[coords[0]][coords[1]] = value

            if generate_grid(board):
                return True
            else:
                board[coords[0]][coords[1]] = 0

    return False