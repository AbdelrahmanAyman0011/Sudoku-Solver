import pygame
from solver import solve, valid, print_board  # Import your solver functions

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 540, 600
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)

# Set up the window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

# Font
font = pygame.font.Font(None, 40)

# Function to draw the Sudoku grid
def draw_grid(board, selected):
    for i in range(GRID_SIZE + 1):
        thickness = 4 if i % 3 == 0 else 1
        pygame.draw.line(win, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), thickness)
        pygame.draw.line(win, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WIDTH), thickness)

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] != 0:
                text = font.render(str(board[i][j]), True, BLACK)
                win.blit(text, (j * CELL_SIZE + 15, i * CELL_SIZE + 10))

    if selected:
        col, row = selected
        pygame.draw.rect(win, RED, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)

# Function to update the board based on user input
def get_input(selected, board, key):
    col, row = selected
    if selected and 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE and key.isdigit() and 1 <= int(key) <= 9:
        if valid(board, int(key), (row, col)):  # Check if the input is valid for the selected cell
            board[row][col] = int(key)

# Main game loop
def main():
    board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]  # Initialize an empty board
    selected = None  # Selected cell

    running = True
    solving = False

    solving_button = pygame.Rect(200, 550, 140, 40)  # Create a solving button
    solving_text = font.render("Solve", True, BLACK)

    while running:
        win.fill(WHITE)
        draw_grid(board, selected)

        pygame.draw.rect(win, GRAY, solving_button)  # Draw the button
        win.blit(solving_text, (solving_button.x + 40, solving_button.y + 10))  # Position the text


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // CELL_SIZE
                row = y // CELL_SIZE
                selected = (col, row)
                if solving_button.collidepoint(x, y):  # Check if the button was clicked
                    solve(board)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solving = True
                elif event.key == pygame.K_RETURN:
                    solving = False
                    print_board(board)  # Print the current board (for testing purposes)
                elif event.key == pygame.K_c:
                    board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]  # Clear the board
                elif event.key == pygame.K_BACKSPACE:
                    col, row = selected
                    if board[row][col] == 0:
                        board[row][col] = 0
                elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                    if selected:
                        num = int(pygame.key.name(event.key))  # Get the number from the key
                        get_input(selected, board, str(num))  # Pass the number as a string to get_input
                        selected = None

        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
