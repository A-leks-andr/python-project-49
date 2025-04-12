import prompt
from random import randint


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def get_gcd(name):
    print('Find the greatest common divisor of given numbers.')

    for i in range(3):
        a = randint(1, 50)
        b = randint(2, 50)
        check = str(gcd(a, b))
        print(f'Question: {a} {b}')
        answer = prompt.string('Your answer: ')
        if answer == check:
            print('Correct')
        else:
            print(f" '{answer}' is wrong answer ;(. ",
              f"Correct answer was '{check}'.")
            print(f"Let's try again, {name}")
            break

    else:
        print(f'Congratulations, {name}')