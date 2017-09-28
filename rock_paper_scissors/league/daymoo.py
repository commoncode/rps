import random
from rock_paper_scissors import ROCK, PAPER, SCISSORS, BasePlayer


class Player(BasePlayer):

    player_name = 'Daymoo'
    author = 'Daymon'

    def __init__(self, start_play=PAPER):
        self.next_play = start_play

    def play(self):
        """
        Must return a single var for the decided play:
        either 'ROCK', 'PAPER', 'SCISSORS'
        """
        self.next_play = random.choice(
            [ROCK, SCISSORS, PAPER]
        )

        return self.next_play

    def result(self, their_play):
        self.next_play = their_play
