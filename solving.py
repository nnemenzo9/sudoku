# Contains solving functions

# TODO: Optimize solving
# TODO: Calculate difficulty scores using branch-factor

import global_var

# Board is a numpy array; solve() is only called one time
def solve(board):    
    # It findEmptyCell returns 'none', there are no more empty cells and the program is complete
    # If find empty cell does not return none, we need to find new coordinates.
    if not find_empty_cell(board):
        return True
    else: 
        coords = find_empty_cell(board)


    for value in range(1, 10):
        # If value is valid in the certain cell it will place the value in the board and call solve() again.
        if check_if_valid(board, coords, value):
            board[coords[0]][coords[1]] = value

            # Recursive solving; if solve() returns true (findEmptyCell returns true), the program is complete
            if solve(board):
                return True
            else:
                # If solve is false (no possible value), we backtrack.
                board[coords[0]][coords[1]] = 0

    # At this point, we have gone through all possible values 
    return False

# Function that checks if there are still empty cells in the grid
def check_grid(board):
    for r in range(global_var.DIMENSIONS):
        for c in range(global_var.DIMENSIONS):
            if board[r][c] == 0:
                return True
    return False

# Function that finds the first empty cell 
def find_empty_cell(board):
    for r in range(global_var.DIMENSIONS):
        for c in range(global_var.DIMENSIONS):
            if board[r][c] == 0:
                return (r, c)
    return None 

"""
def get_candidate_values(board, coords):
    POSSIBLE_VALUES = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    # Go through columns
    for i in range(global_var.DIMENSIONS):
        if board[i][coords[1]] in POSSIBLE_VALUES:
            POSSIBLE_VALUES.remove(board[i][coords[1]])

    # Go through rows
    for i in range(global_var.DIMENSIONS):
        if board[coords[0]][i] in POSSIBLE_VALUES:
            POSSIBLE_VALUES.remove(board[coords[0]][i])

    # Go through subgrid
    starting_r = (coords[0] // global_var.SUBGRIDS) * global_var.SUBGRIDS
    starting_c = (coords[1] // global_var.SUBGRIDS) * global_var.SUBGRIDS
    for r in range(global_var.SUBGRIDS):
        for c in range(global_var.SUBGRIDS):
            if board[starting_r + r][starting_c + c] in POSSIBLE_VALUES:
                POSSIBLE_VALUES.remove(board[starting_r + r][starting_c + c])

    return POSSIBLE_VALUES
"""


# Return true if no matching value found, false if matching value found.
# 'coords' is a tuple that holds the coordinates of a certain cell in (row, column).
def check_if_valid(board, coords, value):
    # Check columns
    for i in range(global_var.DIMENSIONS):
            if value == board[i][coords[1]] and coords[0] != i: # make sure we aren't checking the same cell
                return False

    # Check rows
    for i in range(global_var.DIMENSIONS):
        if value == board[coords[0]][i] and coords[1] != i:
            return False

    # Check subgrids
    starting_r = (coords[0] // global_var.SUBGRIDS) * global_var.SUBGRIDS
    starting_c = (coords[1] // global_var.SUBGRIDS) * global_var.SUBGRIDS
    for r in range(global_var.SUBGRIDS):
        for c in range(global_var.SUBGRIDS):
            if board[starting_r + r][starting_c + c] == value and (r, c) != coords:
                return False
    
    return True

if __name__ == "__main__":
    main()
