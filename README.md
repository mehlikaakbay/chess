# Chess Game

This project is an enhanced chess game implemented in **Python 3.13** using the **Pygame** library. It features a user-friendly graphical interface and implements key chess rules, including movement validation, check, checkmate, and stalemate detection. The game provides a visually engaging experience with additional features like captured pieces display and move history.


## **Team Members**

- **Ipek Zobu**, Student ID: 30971700  
- **Ada Alkim Acikyol**, Student ID: 28576498  
- **Mehlika Rana Akbay**, Student ID: 51259883  


## **Prerequisites**

Ensure you have the following installed on your system:

- **Python 3.13**  
- **Pygame library**

To install Pygame, run:

```bash
pip install pygame
```


## **How to Run**

1. Download or clone the project files, ensuring the `assets` folder contains the following image files:
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

3. Run the game with:

```bash
python main.py
```


## **Gameplay Instructions**

- The game starts with **White's turn**.  
- **Selecting Pieces:**
  - Click on a piece to select it. Valid moves will be highlighted.  
  - Click on a highlighted square to move the piece.
- **Turn Management:**
  - Turns alternate between White and Black players.  
- **Rules Enforced:**
  - Legal movement validation for all pieces.  
  - Detection of check, checkmate, and stalemate.  
- The game ends when:
  - A **checkmate** occurs.
  - A **stalemate** occurs.  
  - A player resigns or manually exits.  


## **Features**

### **New Enhancements**
1. **Graphical Interface Improvements:**
   - A larger game screen (1000x800) with a sidebar for additional game details.
   - Sidebar includes:
     - **Captured Pieces Display:** Shows captured pieces for both players.
     - **Current Turn Display:** Highlights whose turn it is.

2. **Real-Time Highlights:**
   - Valid moves are visually highlighted for the selected piece.
   - The king is highlighted in red when in check.

3. **Game State Management:**
   - Detection and handling of **check**, **checkmate**, and **stalemate**.
   - Prevents moves that place the king in check.

4. **Move History:**
   - Displays the last 10 moves for quick reference.

### **Core Features**
- **Accurate Movement Logic:**
  - Handles specific movements for pawns, rooks, bishops, knights, queens, and kings.
  - Prevents illegal moves and self-check.
- **User-Friendly Design:**
  - Mouse hover effects on squares.
  - Clear messages for game-ending scenarios.


## **Assumptions and Limitations**

- **Rules Implemented:**
  - Basic chess rules are enforced.
  - Advanced rules such as **castling**, **en passant**, and **pawn promotion** are **not yet implemented**.
- **Game Save/Resume:** Not currently supported.
- **Compatibility:** Designed for Python 3.13. Other versions may not work correctly.


## **Future Enhancements**

The project can be further expanded with the following features:
- Implementation of advanced chess rules (e.g., castling, en passant).
- Save/load functionality to resume games.
- Multiplayer support over a network or local hotseat mode.


## **Acknowledgments**

This project is the result of a collaborative effort and serves as an educational exploration of Python, Pygame, and chess logic implementation.

