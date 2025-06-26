from brain_games.engine import run_game
from brain_games.games.even import generate_round, get_description


def main():
    game_description = get_description()
    run_game(game_description, generate_round)
