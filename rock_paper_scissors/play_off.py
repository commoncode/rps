from . import ROCK, PAPER, SCISSORS, DRAW, LOSE, WIN
from collections import namedtuple


result_table = {
    ROCK: {
        ROCK: DRAW,
        PAPER: LOSE,
        SCISSORS: WIN,
    },
    PAPER: {
        ROCK: WIN,
        PAPER: DRAW,
        SCISSORS: LOSE,
    },
    SCISSORS: {
        ROCK: LOSE,
        PAPER: WIN,
        SCISSORS: DRAW,
    }
}

player_data = namedtuple('PlayerData', ['player1', 'player2'])


class PlayOff(object):

    def __init__(self, player1, player2):
        self.player1 = player1()
        self.player2 = player2()
        self.p1_wins = 0
        self.p2_wins = 0
        self.played_rounds = 0

    @property
    def draws(self):
        return self.played_rounds - self.p1_wins - self.p2_wins

    @property
    def p1_losses(self):
        return self.p2_wins

    @property
    def p2_losses(self):
        return self.p1_wins

    def gen_rounds(self, rounds=None):

        if rounds:
            for _ in range(rounds):
                yield self.play_round()
        else:
            while True:
                yield self.play_round()

    def play_rounds(self, rounds=None):
        for _ in self.gen_rounds(rounds=rounds):
            pass

    def play_round(self):

        play = player_data(
            player1=self.player1.play(),
            player2=self.player2.play()
        )

        result = player_data(
            player1=result_table[play.player1][play.player2],
            player2=result_table[play.player2][play.player1]
        )

        self.played_rounds += 1
        if result.player1 == WIN:
            self.p1_wins += 1
        elif result.player2 == WIN:
            self.p2_wins += 1

        self.player1.result(play.player2)
        self.player2.result(play.player1)

        return play, result
