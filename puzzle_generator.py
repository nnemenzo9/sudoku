# Takes generated puzzle and strips away values, making sure the puzzle is still uniquely solvable

# TODO: Change generation so it generates based on branch-factor difficulty.

"""
Stripping values without having to modify the solver too much: 
- For a certain amount of iterations: 
    - Take in the full solution grid
    - Strip a random value from the board and save the value
    - Run solve() on the board with the condition that the value we took out can't be used on the SQUARE THAT IT GOT TAKEN OUT OF
        - If solve() returns true, it has found a solution that differs from our original solution.
            - Therefore, we must put the value back because it compromises the 'uniqueness' of the board
        - If solve() returns false, it hasn't found a solution.
            - We can take the value out 


"""

import random as r
import global_var
import solving as s
from copy import copy, deepcopy

# Based on iterations, the more iterations, the harder the puzzle will be
def strip_values(board):
    max_iterations = 49
    iterations = 0
    while iterations < max_iterations:
        # Gets random coordinates that are filled, saves the value inside and removes that value from the board
        random_coords = get_random_filled_cell(global_var.NEW_BOARD)
        removed_value = board[random_coords[0]][random_coords[1]]
        board[random_coords[0]][random_coords[1]] = 0

        # If a solution has been found with new constraints, put the value back
        if mod_solver(board, removed_value, random_coords):
            board[random_coords[0]][random_coords[1]] = removed_value

            # While mod_solver() finds a solution, keep picking random coords and taking values out
            while mod_solver(board, removed_value, random_coords): 
                random_coords = get_random_filled_cell(global_var.NEW_BOARD)
                removed_value = board[random_coords[0]][random_coords[1]]
                board[random_coords[0]][random_coords[1]] = 0

                # If mod_solver() returns false, add 1 to iterations and break
                if not mod_solver(board, removed_value, random_coords):
                    iterations += 1
                    break

        # No solution has been found (puzzle is still uniquely solvable and we permanently strip the value)
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


def mod_solver(board, removed_value, removed_value_coords):

    # Copy the board so we don't change the actual board
    board_copy = deepcopy(board)

    if not s.find_best_empty_cell(board_copy):
        return True
    else: 
        coords = s.find_best_empty_cell(board_copy)

    # Generate the possible values in a cell
    VALUES = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    # If solve() is currently on the same square that the the value recently got removed, we can't place that value back in.
    if coords == removed_value_coords:
        VALUES.remove(removed_value)

    # Run through possible values
    for value in VALUES:
        if s.check_if_valid(board_copy, coords, value):
            board_copy[coords[0]][coords[1]] = value

            if mod_solver(board_copy, removed_value, removed_value_coords):
                return True
            else:
                board_copy[coords[0]][coords[1]] = 0
    
    return False