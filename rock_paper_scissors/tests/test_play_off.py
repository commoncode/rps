
from itertools import cycle
import unittest
from unittest import mock

from rock_paper_scissors.play_off import PlayOff
from rock_paper_scissors import ROCK, PAPER, SCISSORS, DRAW, WIN, LOSE


class MockPlayer(mock.Mock):

    def play(self):
        return ROCK

    def result(self, their_play):
        pass


class MockPlayer1(MockPlayer):
    pass


class MockPlayer2(MockPlayer):
    pass


class TestPlayOffProperties(unittest.TestCase):

    def setUp(self):
        self.play_off = PlayOff(player1=MockPlayer, player2=MockPlayer)
        self.play_off.p1_wins = 5
        self.play_off.p2_wins = 10
        self.play_off.played_rounds = 20

    def test_player1_losses(self):
        self.assertEqual(self.play_off.p1_losses, self.play_off.p2_wins)

    def test_player2_losses(self):
        self.assertEqual(self.play_off.p2_losses, self.play_off.p1_wins)

    def test_draws(self):
        self.assertEqual(
            self.play_off.draws,
            self.play_off.played_rounds - self.play_off.p1_wins - self.play_off.p2_wins
        )


class TestPlayOffCreate(unittest.TestCase):

    def test_create_non_optional(self):
        play_off = PlayOff(MockPlayer, MockPlayer)
        self.assertEqual(play_off.p1_wins, 0)
        self.assertEqual(play_off.p2_wins, 0)
        self.assertEqual(play_off.played_rounds, 0)

    def test_player1_is_player1(self):
        play_off = PlayOff(MockPlayer1, MockPlayer2)
        self.assertIsInstance(play_off.player1, MockPlayer1)

    def test_player2_is_player2(self):
        play_off = PlayOff(MockPlayer1, MockPlayer2)
        self.assertIsInstance(play_off.player2, MockPlayer2)


class TestPlayOffRound(unittest.TestCase):

    def setUp(self):
        self.play_off = PlayOff(player1=MockPlayer1, player2=MockPlayer2)

    def test_play_called_once_on_p1(self):
        self.play_off.player1.play = mock.Mock(return_value=ROCK)
        self.play_off.play_round()
        self.play_off.player1.play.assert_called_once()

    def test_play_called_once_on_p2(self):
        self.play_off.player2.play = mock.Mock(return_value=ROCK)
        self.play_off.play_round()
        self.play_off.player2.play.assert_called_once()

    def test_result_called_once_on_p1(self):
        self.play_off.player1.result = mock.Mock()
        self.play_off.play_round()
        self.play_off.player1.result.assert_called_once()

    def test_result_called_once_on_p2(self):
        self.play_off.player2.result = mock.Mock()
        self.play_off.play_round()
        self.play_off.player2.result.assert_called_once()

    def test_test_round_updated(self):
        self.play_off.play_round()
        self.assertEqual(self.play_off.played_rounds, 1)

    def test_p1_win_updated(self):
        self.play_off.player1.play = mock.Mock(return_value=PAPER)
        self.play_off.play_round()
        self.assertEqual(self.play_off.p1_wins, 1)

    def test_p1_loss_not_updated(self):
        self.play_off.player2.play = mock.Mock(return_value=PAPER)
        self.play_off.play_round()
        self.assertEqual(self.play_off.p1_wins, 0)

    def test_p1_draw_not_updated(self):
        self.play_off.play_round()
        self.assertEqual(self.play_off.p1_wins, 0)

    def test_p2_win_updated(self):
        self.play_off.player2.play = mock.Mock(return_value=PAPER)
        self.play_off.play_round()
        self.assertEqual(self.play_off.p2_wins, 1)

    def test_p2_loss_not_updated(self):
        self.play_off.player1.play = mock.Mock(return_value=PAPER)
        self.play_off.play_round()
        self.assertEqual(self.play_off.p2_wins, 0)

    def test_p2_draw_not_updated(self):
        self.play_off.play_round()
        self.assertEqual(self.play_off.p2_wins, 0)

    def test_round_return_play(self):
        play, _ = self.play_off.play_round()
        self.assertEqual(play.player1, ROCK)
        self.assertEqual(play.player2, ROCK)

    def test_round_return_result(self):
        _, result = self.play_off.play_round()
        self.assertEqual(result.player1, DRAW)
        self.assertEqual(result.player2, DRAW)


class TestPlayOffRounds(unittest.TestCase):

    def setUp(self):
        self.play_off = PlayOff(player1=MockPlayer1, player2=MockPlayer2)
        self.play_off.player1.play = mock.Mock(side_effect=cycle([PAPER, SCISSORS, ROCK]))

    def rounds_played(self, rounds):
        for _ in self.play_off.gen_rounds(rounds=rounds):
            pass

        self.assertEqual(self.play_off.played_rounds, rounds)

    def test_1_round(self):
        self.rounds_played(1)

    def test_10_round(self):
        self.rounds_played(10)

    def test_143_round(self):
        self.rounds_played(143)

    def test_rounds_yield(self):
        play, result = next(self.play_off.gen_rounds())
        self.assertEqual(play.player1, PAPER)
        self.assertEqual(play.player2, ROCK)
        self.assertEqual(result.player1, WIN)
        self.assertEqual(result.player2, LOSE)


if __name__ == '__main__':
    unittest.main()
