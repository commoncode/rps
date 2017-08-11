import time
from itertools import cycle
from unittest import TestCase, mock

from rock_paper_scissors import PLAYS, ROCK
from rock_paper_scissors.league import cycler, reflector, doublereflector, rando


class TestPlayer(TestCase):

    def setUp(self):
        self.player = mock.Mock()
        self.player.play = lambda: ROCK
        self.player.result = lambda _: None
        self.player.author = 'Testy Mc Testface'
        self.player.player_name = "MC Test"

    def test_playing_gives_valid_play(self):
        for __ in range(10000):
            TestCase.assertIn(self, self.player.play(), PLAYS)

    def test_playing_is_short(self):
        start = time.clock()
        for __ in range(10000):
            self.player.play()
        time_delta = time.clock() - start
        TestCase.assertLessEqual(self, time_delta, 0.1)

    def test_player_accepts_result(self):
        plays = cycle(PLAYS)
        for __ in range(10000):
            self.player.result(next(plays))

    def test_result_acceptance_is_short(self):
        start = time.clock()
        plays = cycle(PLAYS)
        for __ in range(10000):
            self.player.result(next(plays))
        time_delta = time.clock() - start
        TestCase.assertLessEqual(self, time_delta, 0.1)

    def test_has_string_author(self):
        TestCase.assertIsInstance(self, self.player.author, str)

    def test_has_string_player_name(self):
        TestCase.assertIsInstance(self, self.player.player_name, str)


class TestPlayer1(TestPlayer):
    def setUp(self):
        self.player = reflector.Player()


class TestPlayer2(TestPlayer):
    def setUp(self):
        self.player = cycler.Player()


class TestPlayer3(TestPlayer):
    def setUp(self):
        self.player = doublereflector.Player()


class TestPlayer4(TestPlayer):
    def setUp(self):
        self.player = rando.Player()
