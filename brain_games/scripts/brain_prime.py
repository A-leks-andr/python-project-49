from brain_games.game_prime import is_prime
from brain_games.greet_name import greet_and_name


def main():
    name = greet_and_name()
    is_prime(name)


if __name__ == "__main__":
    main()
