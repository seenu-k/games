"Tic Tac Toe Game Implementation"

import numpy as np

from base.game import BaseGame, BaseState, GameConfiguration

class TicTacToeConfiguration(GameConfiguration):
    "Tic Tac Toe Configuration"
    def __init__(self, size=3):
        super().__init__()
        self.size = size

class TicTacToeState(BaseState):
    "Tic Tac Toe Game State"

    def __init__(self, board):
        super().__init__()
        self._board = board
        self._is_winning = None


    def legal_moves(self):
        "Return empty squares"
        if self.is_winning():
            return tuple()
        return tuple(map(tuple, np.argwhere(self._board == -1)))

    def is_winning(self):
        "Check if the state is a winning state"
        if self._is_winning is None:
            self._is_winning = False, None
            for player in (0, 1):
                row_win = np.any(np.all(self._board == player, axis=1))
                column_win = np.any(np.all(self._board == player, axis=0))
                primary_diagonal_win = np.all(np.diagonal(self._board) == player)
                secondary_diagonal_win = np.all(np.diagonal(np.fliplr(self._board)) == player)
                if row_win or column_win or primary_diagonal_win or secondary_diagonal_win:
                    self._is_winning = True, player
        return self._is_winning


class TicTacToe(BaseGame):
    "Tic Tac Toe Game"

    def __init__(self, config = None):
        if config is None:
            config = TicTacToeConfiguration()
        initial_state = TicTacToeState(np.full((config.size, config.size), -1, dtype=np.int8))
        super().__init__(initial_state=initial_state, config=config)

    def update(self, state, action):
        board = self.state.board.copy()
        board[action] = self.state.current_player
        updated_state = TicTacToeState(board)
        next_player = (self.state.current_player + 1) % self.config.number_of_players
        updated_state.current_player = next_player
        return updated_state


if __name__ == "__main__":
    game = TicTacToe()
    moves = ((0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2))
    for move in moves:
        print(game.play(move))
    print(game.state.board)
