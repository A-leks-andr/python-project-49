from random import randint

import prompt


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
            check = 'yes'
        else:
            check = 'no'
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if answer == check:
            print('Correct!')
        else:
            print(f" '{answer}' is wrong answer ;(. ",
              f"Correct answer was '{check}'.")
            print(f"Let's try again, {name}!")
            break

    else:
        print(f'Congratulations, {name}!')