from brain_games.game_calc import get_calc
from brain_games.greet_name import greet_and_name


def main():
    name = greet_and_name()
    get_calc(name)


if __name__ == "__main__":
    main()
