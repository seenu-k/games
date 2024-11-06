"Abstract Base Classes for Games"

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from collections import deque

@dataclass
class GameConfiguration:
    "Configuration for a game"
    number_of_players = 2
    state_history = None


class BaseState(ABC):
    "Abstract state of a game"

    def __init__(self):
        self.current_player = 0

    @abstractmethod
    def legal_moves(self):
        "Returns legal moves in the state"
        raise NotImplementedError

    @abstractmethod
    def is_winning(self):
        "Returns whether the state is winning and the winning player"
        raise NotImplementedError


class BaseGame(ABC):
    "Abstract game"

    def __init__(self, initial_state, config = None):
        self.config = config or GameConfiguration()
        self.history = deque(maxlen=self.config.state_history)
        self.history.append(initial_state)

    @property
    def state(self):
        "Return the current state of the game"
        return self.history[-1]

    @abstractmethod
    def update(self, state, action):
        "Return a new state applying action on state"
        raise NotImplementedError

    def legal_moves(self):
        "Returns legal moves in the curent game position"
        return self.state.legal_moves()

    def is_legal(self, move):
        "Checks whether a move is legal"
        return move in self.legal_moves()

    def play(self, move):
        "Plays a move and returns the updated state"
        if self.state is None:
            logging.error("State is not initialised")
            return
        if not self.is_legal(move):
            logging.error("Move is not a legal move")
            return
        updated_state = self.update(self.state, move)
        self.history.append(updated_state)
        return updated_state.is_winning()
