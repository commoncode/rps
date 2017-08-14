from itertools import cycle
import time
import unittest

from rock_paper_scissors import PLAYS
from rock_paper_scissors.main import load_from_players_module

PLAYERS = load_from_players_module()


def pytest_generate_tests(metafunc):

    test_names = [
        scenario['source']
        for scenario in metafunc.cls.scenarios
    ]
    scenario_values = [
        [scenario['class']]
        for scenario in metafunc.cls.scenarios
    ]

    metafunc.parametrize(
        argnames=['player_class'],
        argvalues=scenario_values,
        ids=test_names,
        scope="class")


class TestLoadedPlayers(object):
    scenarios = [
        {
            'source': player_info[0],
            'class': player_info[1]
        }
        for player_info in PLAYERS
    ]

    def test_has_string_author(self, player_class):
        player = player_class()
        assert isinstance(player.author, str)

    def test_has_string_player_name(self, player_class):
        player = player_class()
        assert isinstance(player.player_name, str)

    def test_playing_gives_valid_play(self, player_class):
        player = player_class()
        for __ in range(10000):
            assert player.play() in PLAYS

    def test_playing_is_short(self, player_class):
        player = player_class()
        start = time.clock()
        for __ in range(10000):
            player.play()
        time_delta = time.clock() - start
        assert time_delta <= 0.1

    def test_player_accepts_result(self, player_class):
        player = player_class()
        plays = cycle(PLAYS)
        for __ in range(10000):
            player.result(next(plays))

    def test_result_acceptance_is_short(self, player_class):
        player = player_class()
        start = time.clock()
        plays = cycle(PLAYS)
        for __ in range(10000):
            player.result(next(plays))
        time_delta = time.clock() - start
        assert time_delta <= 0.1


class TestPlayerNames(unittest.TestCase):

    def test_unique_names(self):
        unique_names = set()
        for module_name, player_class in PLAYERS:
            name = player_class.player_name
            assert name not in unique_names, \
                'Player name "{}" in "{}" is not unique'.format(
                    name,
                    module_name
                )
            unique_names.add(name)
