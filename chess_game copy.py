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


# Function to draw the board with highlighting
def draw_board_with_highlight():
    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()
    hover_col = mouse_pos[0] // 100
    hover_row = mouse_pos[1] // 100

    for row in range(8):
        for col in range(8):
            color = PRISTINE if (row + col) % 2 == 0 else DARK_RED
            pygame.draw.rect(screen, color, pygame.Rect(col * 100, row * 100, 100, 100))

            if row == hover_row and col == hover_col:
                # Draw a border around the square the mouse is hovering over
                border_rect = pygame.Rect(col * 100, row * 100, 100, 100)
                pygame.draw.rect(screen, HIGHLIGHT_COLOR, border_rect, 5)  # 5px border width


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
            for i in range(min(row_start, row_end) + 1, max(row_start, row_end)):
                if board[i][col_start]:
                    return False
            return True
        elif row_start == row_end:  # Horizontal move
            for i in range(min(col_start, col_end) + 1, max(col_start, col_end)):
                if board[row_start][i]:
                    return False
            return True
    # Knight movement (L-shape)
    elif selected_piece == "N":
        if abs(row_start - row_end) == 2 and abs(col_start - col_end) == 1 or abs(row_start - row_end) == 1 and abs(
                col_start - col_end) == 2:
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
            for i in range(min(row_start, row_end) + 1, max(row_start, row_end)):
                if board[i][col_start]:
                    return False
            return True
        elif row_start == row_end:  # Horizontal move
            for i in range(min(col_start, col_end) + 1, max(col_start, col_end)):
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


# Function to check for check
def is_in_check(board, player):
    # Simplified check: check if the player's king is under attack
    king_pos = None
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece and piece[1] == "K" and piece[0] == player:
                king_pos = (row, col)
                break
    if king_pos is None:
        return False

    # Check if any opponent piece can attack the king
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece and piece[0] != player:
                if valid_move(piece, (row, col), king_pos, board):
                    return True
    return False


# Function to check for checkmate
def is_checkmate(board, player):
    if not is_in_check(board, player):
        return False

    # Check if the player can make any valid move
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece and piece[0] == player:
                for r in range(8):
                    for c in range(8):
                        if valid_move(piece, (row, col), (r, c), board):
                            return False
    return True


# Game loop
def game_loop():
    global selected_piece, selected_position, current_turn

    board = START_BOARD
    running = True

    while running:
        screen.fill((0, 0, 0))

        draw_board_with_highlight()
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
                    else:
                        selected_piece = None
                elif piece and piece[0] == current_turn:
                    selected_piece = piece
                    selected_position = (row, col)

        # Check for check and checkmate
        if is_in_check(board, current_turn):
            print(f"{current_turn} is in check!")
            if is_checkmate(board, current_turn):
                print(f"{current_turn} is in checkmate!")
                running = False

        # Check for King capture
        white_king = False
        black_king = False
        for row in range(8):
            for col in range(8):
                piece = board[row][col]
                if piece == "wK":
                    white_king = True
                elif piece == "bK":
                    black_king = True

        if not white_king or not black_king:
            print("Game Over! King captured.")
            running = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()


# Run the game
if __name__ == "__main__":
    game_loop()