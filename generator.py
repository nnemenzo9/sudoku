# Will solve Sudoku puzzles and be used in Sudoku puzzle generation.

# Board is modeled as 2D numpy array
import basicsudoku as bs
import random as r

# Constants
DIMENSIONS = 9
SUBGRIDS = 3


# Numpy array will be filled with values hand (until another method can be found)
# Basicsudoku is for printing the board, we can use a loop to fill the board with numpy values.
# Create board
board = [
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

#MAIN FUNCTION
def main():
    # Convert array to usable string for basicsudoku
    boardString = boardToString(board)
    formattedBoard = bs.SudokuBoard()
    formattedBoard.symbols = boardString
    print(formattedBoard)
    
    # Solve the puzzle, which will change the boardString
    generate(board)
    print("\n")

    # Print the new completed, formatted board
    boardString = boardToString(board)
    formattedBoard.symbols = boardString
    print(formattedBoard)

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

def generate(board):

    # It findEmptyCell returns 'none', there are no more empty cells and the program is complete
    # If find empty cell does not return none, we need to find new coordinates.
    if not findEmptyCell(board):
        return True
    else: 
        coords = findEmptyCell(board)

    # Generate the possible values in a cell
    POSSIBLE_VALUES = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    # Pick a random value
    while len(POSSIBLE_VALUES) > 0:
        
        # Generate a value and check if its in the set, if its in the set generate a new value
        value = r.randint(1, 10)
        
        # If the value is in possible value, remove value from possible values and continue
        if value in POSSIBLE_VALUES: 
            POSSIBLE_VALUES.remove(value)
        else:             
            # While the value isn't in possible values, keep generating values, and if the value is in possible values, remove the value
            while value not in POSSIBLE_VALUES:
                value = r.randint(1, 10)
                if value in POSSIBLE_VALUES:
                    POSSIBLE_VALUES.remove(value)
                    break
        
        # If value is valid in the certain cell it will place the value in the board and call solve() again.
        if checkIfValid(board, coords, value):
            board[coords[0]][coords[1]] = value

            # Recursive solving; if solve() returns true (findEmptyCell returns true), the program is complete
            if generate(board):
                return True
            else:
                # If generate is false (no possible value), we backtrack.
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
