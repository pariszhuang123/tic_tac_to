class Player:
    """
    Represents a player in the Tic-Tac-Toe game.

    Attributes:
        symbol (str): The symbol representing the player ('X' or 'O').

    Methods:
        get_move(): Gets the player's next move.
    """

    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self):
        """Gets the player's next move."""
        while True:
            try:
                move = input(f"Player {self.symbol}, enter your move (row and column): ")
                x, y = map(int, move.split())
                return x, y
            except ValueError:
                print("Invalid input. Please enter row and column numbers separated by a space.")
