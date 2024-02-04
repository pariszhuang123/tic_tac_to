import logging
from board import Board
from player import Player
from exceptions import InvalidMoveError

logging.basicConfig(level=logging.INFO)

class Game:
    """
    Class to manage the Tic-Tac-Toe game.

    Attributes:
        board (Board): The game board.
        players (list): List of two players participating.
        current_player (int): Index of the current player.

    Methods:
        switch_player(): Switches the current player.
        play(): Main method to start the game.
    """

    def __init__(self):
        self.board = Board()
        self.players = [Player('X'), Player('O')]
        self.current_player = 0

    def switch_player(self):
        """Switches the current player."""
        self.current_player = 1 - self.current_player

    def play(self):
        """Main method to start the game."""
        try:
            while not self.board.is_game_over():
                print(self.board)
                move = self.players[self.current_player].get_move()
                try:
                    self.board.make_move(move, self.players[self.current_player].symbol)
                    self.switch_player()
                except InvalidMoveError as e:
                    logging.error(e)
        except KeyboardInterrupt:
            logging.info("Game interrupted")

        print("Game Over")
        if winner := self.board.get_winner():
            print(f"Player {winner} wins!")
        else:
            print("It's a draw!")

if __name__ == "__main__":
    game = Game()
    game.play()
