import pkgutil
from itertools import combinations
from .play_off import PlayOff
from . import league


class Competition(object):

    def __init__(self, players, game_format):
        self.players = players
        self.scoreboard = {
            player.player_name: 0
            for player in self.players
        }
        self.game_format = game_format

    def run(self, rounds_per_game=10000):
        for game in self.setup_games(self.player_pairs):
            game.play_rounds(rounds=rounds_per_game)
            self.scoreboard[game.player1.player_name] += game.p1_wins
            self.scoreboard[game.player2.player_name] += game.p2_wins

    def setup_games(self, player_pairs):
        return [
            self.game_format(player1, player2)
            for player1, player2 in player_pairs
        ]

    @property
    def player_pairs(self):
        return combinations(self.players, r=2)

    def __str__(self):
        return str(self.scoreboard)
