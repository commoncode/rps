from colorama import init
from abc import ABCMeta, abstractmethod

init()

ROCK = 'ROCK'
PAPER = 'PAPER'
SCISSORS = 'SCISSORS'
WIN = 1
LOSE = -1
DRAW = 0


class BasePlayer(metaclass=ABCMeta):

    @property
    @abstractmethod
    def player_name(self):
        pass

    @property
    @abstractmethod
    def author(self):
        pass

    @abstractmethod
    def play(self):
        pass

    def result(self, their_play):
        pass
