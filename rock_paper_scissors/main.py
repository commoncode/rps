import pkgutil
from rock_paper_scissors import play_off, competitions, league


def load_from_players_module():
    players = list()
    player_modules = pkgutil.walk_packages(path=league.__path__)
    for importer, modname, _ in player_modules:
        player_module = importer.find_module(modname).load_module(modname)
        try:
            player = player_module.Player
        except AttributeError:
            pass
        else:
            players.append((player_module.__name__, player))
    return players


def score_board_print(scoreboard):
    best_to_worst_players = reversed(sorted(scoreboard, key=scoreboard.get))
    print("\nCompetition Results")
    print("-"*32)
    for num, player in enumerate(best_to_worst_players):
        print('{} | {:20s}: {:4s}'.format(num+1, player, str(scoreboard[player])))


def main():
    competition = competitions.Competition(
        players=[player for _, player in load_from_players_module()],
        game_format=play_off.PlayOff
    )
    competition.run()
    score_board_print(competition.scoreboard)
    return 0


if __name__ == '__main__':
    main()
