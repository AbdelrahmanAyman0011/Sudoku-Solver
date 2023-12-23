import pygame
from solver import solve ,valid, print_board  # Import your solver functions

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 540, 600
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Set up the window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

# Font
font = pygame.font.Font(None, 40)

# Function to draw the Sudoku grid
def draw_grid(board):
    for i in range(GRID_SIZE + 1):
        if i % 3 == 0:
            thickness = 4
        else:
            thickness = 1

        pygame.draw.line(win, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), thickness)
        pygame.draw.line(win, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WIDTH), thickness)

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] != 0:
                text = font.render(str(board[i][j]), True, BLACK)
                win.blit(text, (j * CELL_SIZE + 15, i * CELL_SIZE + 10))
            else:
                text = font.render(str(board[i][j]), True, RED)  # Color for empty cells
                win.blit(text, (j * CELL_SIZE + 15, i * CELL_SIZE + 10))
def solve_step_by_step(board):
    solved = solve(board)
    if not solved:
        return False
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if valid(board, num, (i, j)):
                        board[i][j] = num
                        return True
                board[i][j] = 0
                return True
    return True

# Main game loop
def main():
    # Sample Sudoku board
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    running = True
    solving = False
    solving_step_by_step = False

    while running:
        win.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                solving = True

        if solving:
            solve(board)  # Solve the Sudoku puzzle
            solving = False
        if solving_step_by_step:
            solved = solve_step_by_step(board)
            if solved:
                solving_step_by_step = False
        draw_grid(board)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
