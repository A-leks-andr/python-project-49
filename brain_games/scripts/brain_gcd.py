from brain_games.game_gcd import get_gcd
from brain_games.greet_name import greet_and_name


def main():

    name = greet_and_name()
    get_gcd(name)


if __name__ == '__main__':

    main()