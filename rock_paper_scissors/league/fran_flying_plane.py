from rock_paper_scissors import PAPER, SCISSORS, ROCK, BasePlayer


class Player(BasePlayer):

    player_name = 'Flying Plane v2'
    author = 'Fran'
    their_history = []
    choices = [PAPER, SCISSORS, ROCK]
    current_choice = SCISSORS

    def play(self):
        if len(self.their_history) > 1:
            if self.their_history[-1] == self.their_history[-2]:
                self.current_choice = self.their_history[-1]
            else:
                if self.their_history[-1] == PAPER:
                    self.current_choice = ROCK
                elif self.their_history[-1] == ROCK:
                    self.current_choice = SCISSORS
                else:
                    self.current_choice = PAPER
        return self.current_choice

    def result(self, their_play):
        self.their_history.append(their_play)
