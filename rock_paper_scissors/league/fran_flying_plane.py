from rock_paper_scissors import PAPER, BasePlayer


class Player(BasePlayer):

    player_name = 'Flying Plane'
    author = 'Fran'

    def play(self):
        return PAPER
