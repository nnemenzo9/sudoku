# Import files
import basicsudoku as bs
import global_var
import solution_generator as sg
import puzzle_generator as pg
import solving as s


def main():
    # Initialize global variables
    global_var.init()

    # Generate a new solution grid
    sg.generate_grid(global_var.NEW_BOARD)

    # Print formatted new solution grid
    print("\nGenerated solution grid: ")
    print_board(global_var.NEW_BOARD)

    # Strip values from solution grid to create puzzle
    pg.strip_values(global_var.NEW_BOARD)

    # Print new puzzle
    print("\nNew puzzle: ")
    print_board(global_var.NEW_BOARD)


    # Print given puzzle 
    print("\nGiven puzzle: ")
    print_board(global_var.NEW_BOARD)

    # Solve given puzzle
    s.solve(global_var.NEW_BOARD)

    # Print formatted solution to given puzzle
    print("\nSolved puzzle: ")
    print_board(global_var.NEW_BOARD)
    print(s.BRANCH_DIFFICULTY_SCORE)



# Solve a sudoku puzzle
def print_board(board):
    # Convert array to usable string for basicsudoku
    board_string = board_to_string(board)
    formatted_board = bs.SudokuBoard(strict = False)
    formatted_board.symbols = board_string
    print(formatted_board)

# Turn board into string for boardsudoku
def board_to_string(board):
    board_string = str(board)
    board_string = board_string.replace("[", "").replace("]", "").replace("0", ".").replace(",", "").replace(" ", "")
    return board_string

if __name__ == "__main__":
    main()