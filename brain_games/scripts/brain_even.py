from brain_games.game_is_evens import is_evens
from brain_games.greet_name import greet_and_name


def main():
    name = greet_and_name()
    is_evens(name)


if __name__ == '__main__':

    main()