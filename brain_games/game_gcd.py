from random import randint
import prompt
from brain_games.q_and_a import quest_answer


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def get_gcd(name):
    print("Find the greatest common divisor of given numbers.")

    for i in range(3):
        a = randint(1, 50)
        b = randint(2, 50)
        check = str(gcd(a, b))
        quest = f"Question: {a} {b}"
        answer = quest_answer(quest, check, name)
        if answer == "mistake":
            break

    else:
        print(f"Congratulations, {name}!")
