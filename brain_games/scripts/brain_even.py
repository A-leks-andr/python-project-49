from brain_games.game_is_evens import which_evens
from brain_games.greet_name import greet_and_name


def main():
    name = greet_and_name()
    which_evens(name)


if __name__ == "__main__":
    main()
