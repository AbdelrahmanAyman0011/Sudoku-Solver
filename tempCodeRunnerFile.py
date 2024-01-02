def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for val in board[row][col][:]:
        if valid(board, val, (row, col)):
            board[row][col] = [val]

            if solve(board):
                return True

            board[row][col] = [0]  # Reset the last element if the last process is false

    return False

