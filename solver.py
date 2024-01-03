def remove_inconsistent_values(board, arc): # 6  # Removes inconsistent values between two cells in the Sudoku board
    Xi, Xj = arc # Extract the two cells involved in the arc
    revised = False # Initialize a flag to track if values are revised


    if isinstance(board[Xi[0]][Xi[1]], list):  # Check if cell Xi represents a domain of possible values
        for val in board[Xi[0]][Xi[1]][:]: # Iterate through each possible value in cell Xi
            consistent = any(val != val2 for val2 in board[Xj[0]][Xj[1]])  # Check consistency with values in cell Xj

            if not consistent:  # If the value in Xi is inconsistent with Xj
                board[Xi[0]][Xi[1]].remove(val)  # Remove the inconsistent value from cell Xi
                revised = True # Set the flag to indicate that values have been revised

    return revised # Return whether any values were revised in the process


def enforce_arc_consistency(board, arcs): # 5  # Ensure arc consistency in the Sudoku board
    while arcs:   # Continue until all arcs are processed  
        Xi, Xj = arcs.pop(0)  # Extract an arc from the list of arcs  || #arc :=  Contains pairs of cells that are constrained by the Sudoku rules (rows, columns, and sub-grids).
        if remove_inconsistent_values(board, (Xi, Xj)): # Check and remove inconsistent values between arcs
            if len(board[Xi[0]][Xi[1]]) == 0:  # If a cell's domain is empty
                return False
            
            for neighbor in [neigh for neigh in arcs if neigh[1] == Xi]: # For each neighbor of Xi
                arcs.append((neighbor[0], Xi)) # Add new arcs to process based on the updated constraints

    return True # Return True if all arcs are consistent and the board can be solved



def apply_arc_consistency(board): # 4
    arcs = generate_all_arcs()

    while not is_board_solved(board):
        enforce_arc_consistency(board, arcs)
        for i in range(9):
            for j in range(9):
                if len(board[i][j]) == 1:
                    board[i][j] = board[i][j][0]


def remove_inconsistent_values(board, arc): # 7 
    Xi, Xj = arc
    revised = False

    if isinstance(board[Xi[0]][Xi[1]], list):
        for val in board[Xi[0]][Xi[1]][:]:
            consistent = any(val != val2 for val2 in board[Xj[0]][Xj[1]])
            if not consistent:
                board[Xi[0]][Xi[1]].remove(val)
                revised = True

    return revised


def enforce_arc_consistency(board, arcs): # 5
    while arcs:
        Xi, Xj = arcs.pop(0)
        if remove_inconsistent_values(board, (Xi, Xj)):
            if len(board[Xi[0]][Xi[1]]) == 0:
                return False

            for neighbor in [neigh for neigh in arcs if neigh[1] == Xi]:
                arcs.append((neighbor[0], Xi))

    return True


def generate_all_arcs():
    arcs = []
    for i in range(9):
        for j in range(9):            # Generate arcs for cells in the same row, excluding the same cell
            for k in range(9):
                if k != j:# Ensure different columns
                    arcs.append(([i, j], [i, k])) # Add an arc between cells [i, j] and [i, k]
                    
            # Generate arcs for cells in the same column, excluding the same cell
            for k in range(9):
                if k != i:
                    arcs.append(([i, j], [k, j]))

            sub_i, sub_j = 3 * (i // 3), 3 * (j // 3) # it makes sub grid 3 x 3 
            for k in range(sub_i, sub_i + 3):
                for l in range(sub_j, sub_j + 3):
                    if k != i or l != j:
                        arcs.append(([i, j], [k, l]))

    return arcs


def apply_arc_consistency(board):
    arcs = generate_all_arcs()
    enforce_arc_consistency(board, arcs)


def is_board_solved(board): # 8
    for row in board:
        for val in row:
            if isinstance(val, list):
                return False
    return True


def solve(board): # 1  Function to solve the Sudoku puzzle using backtracking
    empty_cell = find_empty_cell(board) # Find an empty cell in the Sudoku board
    if not empty_cell:  # If no empty cells are left, the board is solved
        return True
    else:
        row, col = empty_cell # Get the indices of the empty cell

    for num in range(1, 10): # Try numbers from 1 to 9 in the empty cell
        if is_valid_move(board, num, (row, col)): # Check if placing 'num' is a valid move
            board[row][col] = num # If valid, place 'num' in the cell
            
            # Create a copy of the board to apply arc consistency
            board_copy = [row[:] for row in board] # Make a copy of the current board
            apply_arc_consistency(board_copy) # Apply arc consistency to the copied board

            #display_board(board_copy) display all iterations   <-------

            if is_board_solved(board_copy) and solve(board_copy):
                # Copy back the solved values to the original board
                for i in range(9):
                    for j in range(9):
                        board[i][j] = board_copy[i][j]
                return True # Return True if the puzzle is solved
    
            board[row][col] = 0 # If no solution, reset the cell to 0 for backtracking


    return False


# Rest of the code remains the same



def is_valid_move(board, num, pos): # 3 
    for i in range(len(board[0])):# Check the row for num's presence
        if board[pos[0]][i] == num and pos[1] != i:  # Ensure uniqueness in the row except at 'pos'
            return False

    for i in range(len(board[0])): # Check the column for num's presence
        if board[i][pos[1]] == num and pos[0] != i:  # Ensure uniqueness in the column except at 'pos'
            return False

    y = pos[0] // 3 # Identify the sub-grid's starting row index
    x = pos[1] // 3 # Identify the sub-grid's starting column index

    for i in range(y * 3, y * 3 + 3): # Traverse the sub-grid's rows
        for j in range(x * 3, x * 3 + 3): # Traverse the sub-grid's columns
            if board[i][j] == num and (i, j) != pos: # Ensure uniqueness in the sub-grid except at 'pos'
                return False
    return True


def find_empty_cell(board): # 2
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j
    return None

def valid(board, num, pos): # for GUI
    # check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # check col
    for i in range(len(board[0])):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    # check squre
    y = pos[0] // 3
    x = pos[1] // 3

    for i in range(y * 3, y * 3 + 3):
        for j in range(x * 3, x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

# Initial Sudoku board
board = [
    [5, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 8, 0, 0, 0, 4, 0],
    [7, 0, 6, 0, 0, 3, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 7, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 3, 0, 4, 0, 0, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 6, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 3]
]


def print_board(board):# for GUI
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("------------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def display_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # Separate rows every three rows

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")  # Separate columns every three columns

            if isinstance(board[i][j], list):
                print("[{}]".format(", ".join(str(x) for x in board[i][j])), end=" ")
            else:
                print(board[i][j], end=" ")

        print()

# Display the initial board
print("Initial Sudoku Board:")
display_board(board)

# Solve the Sudoku puzzle
solve(board)

# Display the solved Sudoku board
print("************************")
print("******* Solution *******")
print("************************")
display_board(board)
