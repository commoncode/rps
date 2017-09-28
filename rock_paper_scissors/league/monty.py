import random
from rock_paper_scissors import ROCK, PAPER, SCISSORS, BasePlayer


class Player(BasePlayer):

    player_name = 'Monty'
    author = 'Leonard B'

    def __init__(self):
        self.history = []
        self.current_choice = None
        self.counts = {ROCK: 0, PAPER: 0, SCISSORS: 0}
        self.round = 1

    def play(self):
        """
        Must return a single var for the decided play:
        either 'ROCK', 'PAPER', 'SCISSORS'
        """
        if self.round == 1:
            self.current_choice = random.choice([ROCK, PAPER, SCISSORS])
        else:
            random_number = random.randint(1, self.round)
            if random_number <= self.counts[ROCK]:
                self.current_choice = PAPER
            elif random_number <= self.counts[ROCK] + self.counts[PAPER]:
                self.current_choice = SCISSORS
            else:
                self.current_choice = ROCK
        return self.current_choice

    def result(self, their_play):
        self.history.append((self.current_choice, their_play))
        self.counts[their_play] += 1
        self.round += 1
