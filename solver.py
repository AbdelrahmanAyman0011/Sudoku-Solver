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

def print_board(board):

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("------------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end ="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end ="")



def solve(board):

    find = find_empty(board)
    if not find:
        return True
    else:
        row , col = find

    for i in range(1,10):
        if valid(board , i , (row , col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0 # make the last element 0 if the last process is false

    return False

def valid(board , num , pos):
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
            if board[i][j] == num and (i , j) != pos:
                return False
    return True



def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board [i][j] == 0:
                return (i , j) # zero idx
    return None
print_board(board)
solve(board)
print("************************")
print("******* solution *******")
print("************************")

print_board(board)