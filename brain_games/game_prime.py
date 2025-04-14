from random import randrange

import prompt


def is_prime(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                  47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
    for _ in range(3):
        number = randrange(1, 106, 2)
        if number in prime_list:
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
            print(f"Let's try again, {name}")
            break

    else:
        print(f'Congratulations, {name}')