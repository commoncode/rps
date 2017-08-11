from itertools import cycle
from rock_paper_scissors import ROCK, PAPER, SCISSORS, BasePlayer


class Player(BasePlayer):

    player_name = 'Cycler'
    author = 'Sarah'

    def __init__(self):
        self.plays = cycle([PAPER, ROCK, SCISSORS, PAPER])

    def play(self):
        """
        Must return a single var for the decided play:
        either 'ROCK', 'PAPER', 'SCISSORS'
        """
        return next(self.plays)
