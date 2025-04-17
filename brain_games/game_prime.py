from random import randint
import prompt
from brain_games.q_and_a import quest_answer


def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_prime(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for _ in range(3):
        number = randint(1, 3572)
        if prime(number):
            check = "yes"
        else:
            check = "no"
        quest = f"Question: {number}"
        answer = quest_answer(quest, check, name)
        if answer == "mistake":
            break

    else:
        print(f"Congratulations, {name}!")
