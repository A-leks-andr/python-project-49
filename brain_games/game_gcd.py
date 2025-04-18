from random import randint


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def get_gcd():
    greet = "Find the greatest common divisor of given numbers."

    a = randint(1, 50)
    b = randint(2, 50)
    check = str(gcd(a, b))
    quest = f"Question: {a} {b}"
    return greet, quest, check
