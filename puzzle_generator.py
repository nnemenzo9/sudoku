# Takes generated puzzle and strips away values, making sure the puzzle is still uniquely solvable

# TODO: PUZZLE GENERATION DOES NOT CONSIDER UNIQUENESS, BASICALLY ONLY STRIPS VALUES.

import random as r
import global_var
import solving as s

# Based on iterations, the more iterations, the harder the puzzle will be
def strip_values(board):
    max_iterations = 42
    iterations = 0
    while iterations < max_iterations:
        # Gets random coordinates that are filled, saves the value inside and removes that value from the board
        random_coords = get_random_filled_cell(global_var.NEW_BOARD)
        removed_value = board[random_coords[0]][random_coords[1]]
        board[random_coords[0]][random_coords[1]] = 0

        # If a solution has been found with new constraints, put the value back
        if mod_solver(board, removed_value):
            board[random_coords[0]][random_coords[1]] = removed_value

            # While mod_solver() finds a solution, keep picking random coords and taking values out
            while mod_solver(board, removed_value):
                random_coords = get_random_filled_cell(global_var.NEW_BOARD)
                removed_value = board[random_coords[0]][random_coords[1]]
                board[random_coords[0]][random_coords[1]] = 0

                # If mod_solver() returns false, add 1 to iterations and break
                if not mod_solver(board, removed_value):
                    iterations += 1
                    break

        # No solution has been found (puzzle is still uniquely solvable)
        else: 
            iterations += 1

# Gets a random filled cell to strip the value away
def get_random_filled_cell(board):
    random_coords = (r.randint(0, 8), r.randint(0, 8))
    
    # If cell is empty, keep choosing random cells
    if board[random_coords[0]][random_coords[1]] == 0:
        # Keep choosing cells until one is chosen that is filled
        while board[random_coords[0]][random_coords[1]] == 0:
            random_coords = (r.randint(0, 8), r.randint(0, 8))
            # Cell is filled
            if board[random_coords[0]][random_coords[1]] != 0:
                return random_coords
    else:
        return random_coords

# Checks a solution grid w/ cells removed with the condition that the value that was removed cannot be placed
# Only has to check the first cell for the condition, normal solving after that
cells_counted = 0
def mod_solver(board, removed_value):
    global cells_counted

    if not s.find_empty_cell(board):
        return True
    else: 
        coords = s.find_empty_cell(board)

    for value in range(1, 10):
        
        # Check if the value we're inputting is valid
        if s.check_if_valid(board, coords, value):

            # If iterations is 0, we have to exclude the value in condition checking
            if cells_counted > 0 and value != removed_value:
                board[coords[0]][coords[1]] = value
                
                # Each time we can insert a value, we add one to iterations, since the function moves on to the next square.
                cells_counted += 1

                if mod_solver(board, removed_value):
                    return True
                else:
                    # Each time we backtrack, we remove a value
                    cells_counted -= 1

                    board[coords[0]][coords[1]] = 0
            # If iterations is not 0, don't exclude the value in condition checking
            # If we are on the first cell BUT value != to the removed value, break out of the loop
            elif cells_counted == 0:
                break
            else: 
                board[coords[0]][coords[1]] = value 
                cells_counted += 1
                if mod_solver(board, removed_value):
                    return True
                else:
                    cells_counted -= 1
                    board[coords[0]][coords[1]] = 0
                    print(cells_counted)
    return False
