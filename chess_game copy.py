import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions and colors
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
PRISTINE, DARK_RED = (242, 232, 218), (14, 22, 39)
HIGHLIGHT_COLOR = (200, 200, 0)

# Load chess pieces
PIECES = {
    "wP": pygame.image.load("assets/wP.png"),
    "wR": pygame.image.load("assets/wR.png"),
    "wN": pygame.image.load("assets/wN.png"),
    "wB": pygame.image.load("assets/wB.png"),
    "wQ": pygame.image.load("assets/wQ.png"),
    "wK": pygame.image.load("assets/wK.png"),
    "bP": pygame.image.load("assets/bP.png"),
    "bR": pygame.image.load("assets/bR.png"),
    "bN": pygame.image.load("assets/bN.png"),
    "bB": pygame.image.load("assets/bB.png"),
    "bQ": pygame.image.load("assets/bQ.png"),
    "bK": pygame.image.load("assets/bK.png"),
}

# Resize pieces to fit the board squares
for key in PIECES:
    PIECES[key] = pygame.transform.scale(PIECES[key], (100, 100))

# Initial chessboard setup
START_BOARD = [
    ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
    ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
    ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
]

# Game state variables
selected_piece = None
selected_position = None
current_turn = "w"  # White moves first

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chess Game")


# Function to calculate valid moves for a selected piece
def calculate_valid_moves(piece, position, board):
    valid_moves = []
    for r in range(8):
        for c in range(8):
            if valid_move(piece, position, (r, c), board):
                valid_moves.append((r, c))
    return valid_moves


# Function to draw the board with highlighting
def draw_board_with_highlight(valid_moves=None):
    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()
    hover_col = mouse_pos[0] // 100
    hover_row = mouse_pos[1] // 100

    for row in range(8):
        for col in range(8):
            color = PRISTINE if (row + col) % 2 == 0 else DARK_RED
            pygame.draw.rect(screen, color, pygame.Rect(col * 100, row * 100, 100, 100))

            if valid_moves and (row, col) in valid_moves:
                # Highlight valid move squares
                highlight_rect = pygame.Rect(col * 100, row * 100, 100, 100)
                pygame.draw.rect(screen, HIGHLIGHT_COLOR, highlight_rect, 5)  # 5px border width

            if row == hover_row and col == hover_col:
                # Draw a border around the square the mouse is hovering over
                border_rect = pygame.Rect(col * 100, row * 100, 100, 100)
                pygame.draw.rect(screen, (255, 255, 0), border_rect, 3)  # Yellow hover border


# Function to draw pieces
def draw_pieces(board):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece:
                screen.blit(PIECES[piece], (col * 100, row * 100))


# Function to handle piece movement validation
def valid_move(piece, start, end, board):
    row_start, col_start = start
    row_end, col_end = end
    selected_piece = piece[1]  # Exclude color from piece code (e.g., wP, bP)

    # Prevent moving to a square occupied by the same color piece
    if board[row_end][col_end] and board[row_end][col_end][0] == piece[0]:
        return False

    # Pawn movement
    if selected_piece == "P":
        direction = -1 if piece[0] == "w" else 1
        # Normal move (one square forward)
        if col_start == col_end and board[row_end][col_end] == "" and row_end == row_start + direction:
            return True
        # Initial move (two squares forward)
        if col_start == col_end and board[row_end][col_end] == "" and row_end == row_start + 2 * direction and (
                row_start == 1 or row_start == 6):
            return True
        # Capturing move (diagonal, one square)
        if abs(col_end - col_start) == 1 and row_end == row_start + direction and board[row_end][col_end] and \
                board[row_end][col_end][0] != piece[0]:
            return True
    # Rook movement
    elif selected_piece == "R":
        if col_start == col_end:  # Vertical move
            step = 1 if row_end > row_start else -1
            for i in range(row_start + step, row_end, step):
                if board[i][col_start]:
                    return False
            return True
        elif row_start == row_end:  # Horizontal move
            step = 1 if col_end > col_start else -1
            for i in range(col_start + step, col_end, step):
                if board[row_start][i]:
                    return False
            return True
    # Knight movement (L-shape)
    elif selected_piece == "N":
        if (abs(row_start - row_end) == 2 and abs(col_start - col_end) == 1) or \
           (abs(row_start - row_end) == 1 and abs(col_start - col_end) == 2):
            return True
    # Bishop movement
    elif selected_piece == "B":
        if abs(row_start - row_end) == abs(col_start - col_end):
            r_step = 1 if row_end > row_start else -1
            c_step = 1 if col_end > col_start else -1
            r, c = row_start + r_step, col_start + c_step
            while r != row_end and c != col_end:
                if board[r][c]:
                    return False
                r += r_step
                c += c_step
            return True
    # Queen movement (Rook + Bishop)
    elif selected_piece == "Q":
        if col_start == col_end:  # Vertical move
            step = 1 if row_end > row_start else -1
            for i in range(row_start + step, row_end, step):
                if board[i][col_start]:
                    return False
            return True
        elif row_start == row_end:  # Horizontal move
            step = 1 if col_end > col_start else -1
            for i in range(col_start + step, col_end, step):
                if board[row_start][i]:
                    return False
            return True
        elif abs(row_start - row_end) == abs(col_start - col_end):  # Diagonal move
            r_step = 1 if row_end > row_start else -1
            c_step = 1 if col_end > col_start else -1
            r, c = row_start + r_step, col_start + c_step
            while r != row_end and c != col_end:
                if board[r][c]:
                    return False
                r += r_step
                c += c_step
            return True
    # King movement
    elif selected_piece == "K":
        if abs(row_start - row_end) <= 1 and abs(col_start - col_end) <= 1:
            return True

    return False


# Game loop
def game_loop():
    global selected_piece, selected_position, current_turn

    board = START_BOARD
    running = True
    valid_moves = []

    while running:
        screen.fill((0, 0, 0))

        draw_board_with_highlight(valid_moves)
        draw_pieces(board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                col = event.pos[0] // 100
                row = event.pos[1] // 100
                piece = board[row][col]

                # Select or move piece
                if selected_piece:
                    if valid_move(selected_piece, selected_position, (row, col), board):
                        # Check if destination is not occupied by same colored piece
                        if board[row][col] == "" or board[row][col][0] != selected_piece[0]:
                            board[row][col] = selected_piece
                            board[selected_position[0]][selected_position[1]] = ""
                            selected_piece = None
                            current_turn = "b" if current_turn == "w" else "w"
                            valid_moves = []
                    else:
                        selected_piece = None
                        valid_moves = []
                elif piece and piece[0] == current_turn:
                    selected_piece = piece
                    selected_position = (row, col)
                    valid_moves = calculate_valid_moves(selected_piece, selected_position, board)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


# Run the game
if __name__ == "__main__":
    game_loop()
