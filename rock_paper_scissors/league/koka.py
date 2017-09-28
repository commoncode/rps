import random
from rock_paper_scissors import ROCK, PAPER, SCISSORS, BasePlayer


class Player(BasePlayer):

    player_name = 'Koka'
    author = 'Sourabh K'
    history = []

    def __init__(self, start_play=ROCK):
        self.next_play = start_play

    def play(self):
        if len(self.history) > 3:
            return self.history[len(self.history) - 3]
        else:
            return random.choice([PAPER, ROCK, SCISSORS])

    def result(self, their_play):
        self.history.append(their_play)
