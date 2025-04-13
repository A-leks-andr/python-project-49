from brain_games.game_progression import get_progression
from brain_games.greet_name import greet_and_name


def main():

    name = greet_and_name()
    get_progression(name)


if __name__ == '__main__':

    main()