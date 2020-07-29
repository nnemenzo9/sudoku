# Contains solving functions

# TODO: Optimize solving
# TODO: Calculate difficulty scores

import global_var

# Constants
POSSIBLE_VALUES = {1, 2, 3, 4, 5, 6, 7, 8, 9}

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

# Function that finds the empty cell with the least candidate values 
def find_empty_cell(board):
    for r in range(global_var.DIMENSIONS):
        for c in range(global_var.DIMENSIONS):
            if board[r][c] == 0:
                return (r, c)
    return None

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
    for r in range(3):
        for c in range(3):
            if board[starting_r + r][starting_c + c] == value and (r, c) != coords:
                return False
    
    return True

if __name__ == "__main__":
    main()
