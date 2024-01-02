def revise(board, arc):
    revised = False
    Xi, Xj = arc

    for val in board[Xi[0]][Xi[1]]:
        consistent = False
        for val2 in board[Xj[0]][Xj[1]]:
            if val != val2:
                consistent = True
                break

        if not consistent:
            board[Xi[0]][Xi[1]].remove(val)
            revised = True

    return revised


def arc_consistency(board):
    arcs = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                board[i][j] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            else:
                board[i][j] = [board[i][j]]

    for i in range(len(board)):
        for j in range(len(board[0])):
            # Rows
            for k in range(len(board[0])):
                if k != j:
                    arcs.append(([i, j], [i, k]))

            # Columns
            for k in range(len(board)):
                if k != i:
                    arcs.append(([i, j], [k, j]))

            # Subgrid
            sub_i, sub_j = 3 * (i // 3), 3 * (j // 3)
            for k in range(sub_i, sub_i + 3):
                for l in range(sub_j, sub_j + 3):
                    if k != i or l != j:
                        arcs.append(([i, j], [k, l]))

    while len(arcs) > 0:
        Xi, Xj = arcs.pop(0)
        if revise(board, (Xi, Xj)):
            if len(board[Xi[0]][Xi[1]]) == 0:
                return False

            for neighbor in [neigh for neigh in arcs if neigh[1] == Xi]:
                arcs.append((neighbor[0], Xi))

    return True


def print_board(board):
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


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0  # Reset the last element if the last process is false

    return False


def valid(board, num, pos):
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


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j  # zero idx
    return None


def apply_arc_consistency(board):
    while not is_solved(board):
        arc_consistency(board)
        for i in range(9):
            for j in range(9):
                if len(board[i][j]) == 1:
                    board[i][j] = board[i][j][0]


def is_solved(board):
    for row in board:
        for val in row:
            if isinstance(val, list):
                return False
    return True


# The initial Sudoku board
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

# Display the initial board
print_board(board)

# Apply arc consistency
apply_arc_consistency(board)

# Solve the Sudoku puzzle
solve(board)

# Display the solved Sudoku board
print("************************")
print("******* solution *******")
print("************************")
print_board(board)
