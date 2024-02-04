from exceptions import InvalidMoveError

class Board:
    """
    Represents the Tic-Tac-Toe board.

    Attributes:
        grid (list): 3x3 grid representing the board.
        winner (str): Symbol of the winning player.

    Methods:
        make_move(x, y, symbol): Makes a move on the board.
        is_game_over(): Checks if the game is over.
        get_winner(): Returns the winner's symbol.
    """

    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]
        self.winner = None

    def make_move(self, x, y, symbol):
        """
        Makes a move on the board.
        
        Args:
            x (int): Row index.
            y (int): Column index.
            symbol (str): The player's symbol.
        
        Raises:
            InvalidMoveError: If the move is not valid.
        """
        if not (0 <= x < 3 and 0 <= y < 3 and self.grid[x][y] == ' '):
            raise InvalidMoveError(f"Invalid move at ({x}, {y})")
        self.grid[x][y] = symbol
        self.check_winner(x, y, symbol)

    def is_game_over(self):
        """Checks if the game is over."""
        return self.winner is not None or all(all(cell != ' ' for cell in row) for row in self.grid)

    def get_winner(self):
        """Returns the winner's symbol, if any."""
        return self.winner

    def check_winner(self, x, y, symbol):
        """
        Checks if the current move is a winning move.

        Args:
            x (int): Row index of the move.
            y (int): Column index of the move.
            symbol (str): The player's symbol.
        """
        # Check row, column, and diagonals for a win
        if all(self.grid[x][i] == symbol for i in range(3)) or \
           all(self.grid[i][y] == symbol for i in range(3)) or \
           all(self.grid[i][i] == symbol for i in range(3)) or \
           all(self.grid[i][2-i] == symbol for i in range(3)):
            self.winner = symbol
