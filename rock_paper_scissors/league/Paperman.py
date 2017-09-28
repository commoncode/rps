from rock_paper_scissors import PAPER, SCISSORS, ROCK, BasePlayer
from itertools import cycle


class Player(BasePlayer):

    player_name = 'Loopman'
    author = 'Fran'
    choice = cycle([PAPER, SCISSORS, ROCK])

    def play(self):
        return next(self.choice)

