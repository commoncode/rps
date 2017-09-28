import random
from rock_paper_scissors import ROCK, PAPER, SCISSORS, BasePlayer


class Player(BasePlayer):

    player_name = 'Daymoo'
    author = 'Daymon'

    def __init__(self, start_play=PAPER):
        self.next_play = start_play
        self.their_history = []

    def play(self):

        if len(self.their_history) > 2:
            if self.their_history[-1] == self.their_history[-2] \
                    and self.their_history[-2] == self.their_history[-3]:
                if self.their_history[-1] == SCISSORS:
                    return random.choice([PAPER, ROCK])
                elif self.their_history[-1] == PAPER:
                    return random.choice([SCISSORS, ROCK])
                else:
                    return random.choice([PAPER, SCISSORS])

        if len(self.their_history) > 1:
            if self.their_history[-1] == self.their_history[-2]:
                if self.their_history[-1] == SCISSORS:
                    return random.choice(
                        [PAPER, ROCK]
                    )
                elif self.their_history == PAPER:
                    return random.choice(
                        [SCISSORS, ROCK]
                    )
                else:
                    return random.choice(
                        [PAPER, SCISSORS]
                    )

        if len(self.their_history) > 0:
            if self.their_history[-1] == PAPER:
                return ROCK
            elif self.their_history[-1] == ROCK:
                return SCISSORS
            else:
                return PAPER

        return random.choice(
            [PAPER, SCISSORS, ROCK]
        )

    def result(self, their_play):
        self.their_history.append(their_play)
