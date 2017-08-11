import random
from rock_paper_scissors import ROCK, PAPER, SCISSORS, BasePlayer


class Player(BasePlayer):

    player_name = 'Rando'
    author = 'Brenton C'

    def __init__(self):
        self.history = []
        self.current_choice = None

    def play(self):
        """
        Must return a single var for the decided play:
        either 'ROCK', 'PAPER', 'SCISSORS'
        """
        self.current_choice = random.choice([PAPER, ROCK, SCISSORS, ROCK, ROCK])
        return self.current_choice

    def result(self, their_play):
        self.history.append((self.current_choice, their_play))
