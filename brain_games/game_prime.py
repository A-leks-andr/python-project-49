from random import randint


def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_or_no():
    greet = 'Answer "yes" if given number is prime. Otherwise answer "no".'

    number = randint(1, 3572)
    if prime(number):
        check = "yes"
    else:
        check = "no"

    quest = f"Question: {number}"
    return greet, quest, check
