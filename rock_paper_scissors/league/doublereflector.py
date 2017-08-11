from rock_paper_scissors import ROCK, PAPER, BasePlayer


class Player(BasePlayer):

    player_name = 'DoubleReflector'
    author = 'Sarah'

    def __init__(self, start_plays=None):
        if start_plays is None:
            start_plays = [ROCK, PAPER]

        self.plays = list(start_plays)

    def play(self):
        """
        Must return a single var for the decided play:
        either 'ROCK', 'PAPER', 'SCISSORS'
        """
        return self.plays[-2]

    def result(self, their_play):
        self.plays.append(their_play)
