#Team members

Ipek Zobu, Student ID: 30971700
Ada Alkim Acikyol, Student ID: 28576498
Mehlika Rana Akbay, Student ID: 51259883

# Chess Game

This project is a simplified chess game implemented in Python 3.13 using the Pygame library. It includes a graphical user interface and implements basic chess rules, such as piece movement validation, check, and checkmate detection.

## Prerequisites

Ensure you have the following installed on your system:

- **Python 3.13**
- **Pygame library**

You can install Pygame by running:

```bash
pip install pygame
```

## Running the Game

1. Download or clone the project files, ensuring the `assets` folder containing the following image files is in the same directory as the Python script:
   - `wP.png` (White Pawn)
   - `wR.png` (White Rook)
   - `wN.png` (White Knight)
   - `wB.png` (White Bishop)
   - `wQ.png` (White Queen)
   - `wK.png` (White King)
   - `bP.png` (Black Pawn)
   - `bR.png` (Black Rook)
   - `bN.png` (Black Knight)
   - `bB.png` (Black Bishop)
   - `bQ.png` (Black Queen)
   - `bK.png` (Black King)

2. Open a terminal and navigate to the project directory.

3. Run the script using the following command:

```bash
python main.py
```

## Gameplay Instructions

- The game starts with White's turn.
- Click on a piece to select it. The selected piece will display a highlight border.
- Click on a valid square to move the selected piece.
- Invalid moves are ignored.
- The game enforces chess rules, including:
  - Legal piece movements
  - Check detection
  - Checkmate detection
- The game ends when:
  - A player is checkmated.
  - A king is captured.

## Features

- Graphical user interface with an updated color scheme for the chessboard.
- Real-time highlighting of squares under the mouse pointer.
- Enforcement of basic chess rules (e.g., piece-specific movement, check, and checkmate).
- Immediate detection of game-ending conditions such as checkmate or king capture.

## Assumptions Made

- Only basic chess rules are implemented; advanced rules such as castling, en passant, and pawn promotion are not included.
- The board highlights the square under the mouse pointer.
- Piece movement logic is strictly enforced for pawns, knights, bishops, rooks, queens, and kings.

## Notes

- The game does not support saving or resuming matches.
- The design focuses on simplicity and functionality.
- Ensure Python 3.13 is used, as compatibility with other versions is not guaranteed.