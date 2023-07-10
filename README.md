# Tic-Tac-Toe Game with Minimax Algorithm
This is a simple implementation of the classic game Tic-Tac-Toe, where the computer player uses the Minimax algorithm to make intelligent moves. The game is designed to be played in the command line interface (CLI).

# Prerequisites
To run this game, you need to have the following software installed on your system:
Python (version 3.5 or above)

# Getting Started
Clone the repository or download the source code files.
Open a terminal or command prompt and navigate to the project directory.
Running the Game
To start the Tic-Tac-Toe game, follow these steps:

Open a terminal or command prompt and navigate to the project directory.
Run the following command:
bash
Copy code
python tic_tac_toe.py
The game will start, and you will see the game board displayed on the screen.

# How to Play
The game is played on a 3x3 grid.
The human player is represented by 'X', and the computer player is represented by 'O'.
The human player always goes first.
With each turn, the human player will be prompted to enter the row and column numbers to place their 'X' on the grid.
The grid is numbered from 1 to 9, with the top-left cell 1 and the bottom-right cell 9.
After the human player makes a move, the computer player will automatically make its move.
The game will continue until one player wins or the game ends in a draw.

# Minimax Algorithm
The Minimax algorithm is used by the computer player to determine the best move to make. It works by recursively evaluating all possible moves and selecting the move that maximizes the computer player's chances of winning, while minimizing the human player's chances.

The algorithm assigns a score to each possible move based on the current game state. A positive score indicates a favorable move for the computer player, while a negative score indicates a favorable move for the human player. The computer player selects the move with the highest score.

# Game Outcome
The game can end in one of the following ways:

The human player wins.
The computer player wins.
The game ends in a draw.
After the game ends, you will be prompted to play again or exit the game.

# Customization
If you wish to modify the game or algorithm, you can open the tic_tac_toe.py file in a text editor. The code is well-documented, making it easier to understand and make changes.

# Feedback and Contributions
Feel free to open an issue or submit a pull request on the project's repository if you have any feedback or suggestions.

Enjoy playing Tic-Tac-Toe!
