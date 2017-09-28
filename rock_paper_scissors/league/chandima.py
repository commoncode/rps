from rock_paper_scissors import ROCK, BasePlayer


class Player(BasePlayer):

    player_name = 'rock'
    author = 'chandima'

    def __init__(self, start_play=ROCK):
        self.next_play = start_play

    def play(self):
        """
        Must return a single var for the decided play:
        either 'ROCK', 'PAPER', 'SCISSORS'
        """
        return self.next_play

    def result(self, their_play):
        self.next_play = their_play
