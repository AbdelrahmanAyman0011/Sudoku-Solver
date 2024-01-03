def remove_inconsistent_values(board, arc):
    Xi, Xj = arc
    revised = False

    if isinstance(board[Xi[0]][Xi[1]], list):
        for val in board[Xi[0]][Xi[1]][:]:
            consistent = any(val != val2 for val2 in board[Xj[0]][Xj[1]])
            if not consistent:
                board[Xi[0]][Xi[1]].remove(val)
                revised = True

    return revised


def enforce_arc_consistency(board, arcs):
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
        for j in range(9):
            for k in range(9):
                if k != j:
                    arcs.append(([i, j], [i, k]))

            for k in range(9):
                if k != i:
                    arcs.append(([i, j], [k, j]))

            sub_i, sub_j = 3 * (i // 3), 3 * (j // 3)
            for k in range(sub_i, sub_i + 3):
                for l in range(sub_j, sub_j + 3):
                    if k != i or l != j:
                        arcs.append(([i, j], [k, l]))

    return arcs


def apply_arc_consistency(board):
    arcs = generate_all_arcs()

    while not is_board_solved(board):
        enforce_arc_consistency(board, arcs)
        for i in range(9):
            for j in range(9):
                if len(board[i][j]) == 1:
                    board[i][j] = board[i][j][0]


def remove_inconsistent_values(board, arc):
    Xi, Xj = arc
    revised = False

    if isinstance(board[Xi[0]][Xi[1]], list):
        for val in board[Xi[0]][Xi[1]][:]:
            consistent = any(val != val2 for val2 in board[Xj[0]][Xj[1]])
            if not consistent:
                board[Xi[0]][Xi[1]].remove(val)
                revised = True

    return revised


def enforce_arc_consistency(board, arcs):
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
        for j in range(9):
            for k in range(9):
                if k != j:
                    arcs.append(([i, j], [i, k]))

            for k in range(9):
                if k != i:
                    arcs.append(([i, j], [k, j]))

            sub_i, sub_j = 3 * (i // 3), 3 * (j // 3)
            for k in range(sub_i, sub_i + 3):
                for l in range(sub_j, sub_j + 3):
                    if k != i or l != j:
                        arcs.append(([i, j], [k, l]))

    return arcs


def apply_arc_consistency(board):
    arcs = generate_all_arcs()
    enforce_arc_consistency(board, arcs)


def is_board_solved(board):
    for row in board:
        for val in row:
            if isinstance(val, list):
                return False
    return True


def solve(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    else:
        row, col = empty_cell

    for num in range(1, 10):
        if is_valid_move(board, num, (row, col)):
            board[row][col] = num
            
            # Create a copy of the board to apply arc consistency
            board_copy = [row[:] for row in board]
            apply_arc_consistency(board_copy)
            
            if is_board_solved(board_copy) and solve(board_copy):
                # Copy back the solved values to the original board
                for i in range(9):
                    for j in range(9):
                        board[i][j] = board_copy[i][j]
                return True
    
            board[row][col] = 0

    return False


# Rest of the code remains the same



def is_valid_move(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(board[0])):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    y = pos[0] // 3
    x = pos[1] // 3

    for i in range(y * 3, y * 3 + 3):
        for j in range(x * 3, x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True


def find_empty_cell(board):
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
