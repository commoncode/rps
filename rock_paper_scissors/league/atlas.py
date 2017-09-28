import random
from rock_paper_scissors import ROCK, PAPER, SCISSORS, BasePlayer


class Player(BasePlayer):

    player_name = 'Atlas'
    author = 'Sendhil'

    def __init__(self):
        self.history = []
        self.current_choice = None

    def play(self):
        self.current_choice = random.choice(
            [PAPER, ROCK, SCISSORS, ROCK, PAPER, SCISSORS]
        )
        return self.current_choice

    def result(self, their_play):
        self.history.append((self.current_choice, their_play))
