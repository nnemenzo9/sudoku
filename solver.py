# Will solve Sudoku puzzles and be used in Sudoku puzzle generation.

# Board is modeled as 2D numpy array
import basicsudoku as bs

# Constants
BRANCH_DIFFICULTY_SCORE = 0 # Based on branch factor difficulty 
DIMENSIONS = 9
SUBGRIDS = 3
POSSIBLE_VALUES = {1, 2, 3, 4, 5, 6, 7, 8, 9}


# Numpy array will be filled with values hand (until another method can be found)
# Basicsudoku is for printing the board, we can use a loop to fill the board with numpy values.
# Create board
zeros = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

board = [
        [1, 3, 0, 6, 8, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 6, 0, 0, 1, 9, 0, 3, 8],
        [0, 0, 1, 0, 0, 0, 0, 4, 0],
        [0, 5, 0, 4, 0, 3, 0, 0, 0],
        [3, 0, 0, 8, 0, 0, 0, 0, 6],
        [4, 2, 7, 5, 6, 0, 9, 0, 0],
        [0, 0, 5, 0, 0, 2, 0, 8, 0],
        [0, 8, 0, 0, 0, 7, 0, 0, 0]
    ]

#MAIN FUNCTION
def main():
    # Convert array to usable string for basicsudoku
    boardString = boardToString(board)
    formattedBoard = bs.SudokuBoard()
    formattedBoard.symbols = boardString
    print(formattedBoard)
    
    # Solve the puzzle, which will change the boardString
    solve(board)
    print("\n")

    # Print the new completed, formatted board
    boardString = boardToString(board)
    formattedBoard.symbols = boardString
    print(formattedBoard)

    # Print the branch-difficulty score
    print("Difficulty score: " + str(BRANCH_DIFFICULTY_SCORE))

"""
Basic algorithm:

Iterate through entire board (81 cells) 
    For each cell, generate possible candidate values. 
        Place the first candidate value in the cell and move on to the next square.
            Generate possible candidate values for the next square
                If no possible value, backtrack to the value before and try next candidate value.
    Algorithm is complete when the entire board is finished. 
"""
# Turn board into string for boardsudoku
def boardToString(board):
    boardString = str(board)
    boardString = boardString.replace("[", "").replace("]", "").replace("0", ".").replace(",", "").replace(" ", "")
    return boardString

# Board is a numpy array; solve() is only called one time
def solve(board):
    # Used to calculate the branching factor
    global BRANCH_DIFFICULTY_SCORE
    branching_factor = 1

    # It findEmptyCell returns 'none', there are no more empty cells and the program is complete
    # If find empty cell does not return none, we need to find new coordinates.
    if not findEmptyCell(board):
        return True
    else: 
        coords = findEmptyCell(board)


    for value in range(1, 10):
        # If value is valid in the certain cell it will place the value in the board and call solve() again.
        if checkIfValid(board, coords, value):
            board[coords[0]][coords[1]] = value

            # Recursive solving; if solve() returns true (findEmptyCell returns true), the program is complete
            if solve(board):
                BRANCH_DIFFICULTY_SCORE += (branching_factor - 1) ** 2
                return True
            else:
                # If solve is false (no possible value), we backtrack.
                branching_factor += 1
                board[coords[0]][coords[1]] = 0

    # At this point, we have gone through all possible values 
    return False

def findEmptyCell(board):
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            if board[r][c] == 0:
                return (r, c)
    return None

# Return true if no matching value found, false if matching value found.
# 'coords' is a tuple that holds the coordinates of a certain cell in (row, column).
def checkIfValid(board, coords, value):
    # Check columns
    for i in range(DIMENSIONS):
            if value == board[i][coords[1]] and coords[0] != i: # make sure we aren't checking the same cell
                return False

    # Check rows
    for i in range(DIMENSIONS):
        if value == board[coords[0]][i] and coords[1] != i:
            return False

    # Check subgrids
    startingR = (coords[0] // SUBGRIDS) * SUBGRIDS
    startingC = (coords[1] // SUBGRIDS) * SUBGRIDS
    for r in range(3):
        for c in range(3):
            if board[startingR + r][startingC + c] == value and (r, c) != coords:
                return False
    
    return True

if __name__ == "__main__":
    main()
