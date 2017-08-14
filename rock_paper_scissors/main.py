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


def main():
    competition = competitions.Competition(
        players=[player for _, player in load_from_players_module()],
        game_format=play_off.PlayOff
    )
    competition.run()
    return competition


if __name__ == '__main__':
    main()
