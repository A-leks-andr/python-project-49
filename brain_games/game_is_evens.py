from random import randint

import prompt


def is_evens(name):

    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):

        number = randint(1, 50)
        if number % 2 == 0:
            check = 'yes'
        else:
            check = 'no'

        print('Question:', number)
        answer = prompt.string('Your answer: ')

        if answer == check:
            print('Correct!')

        else:
            print(f'"{answer}" is wrong answer ;(. '
                  f'Correct answer was "{check}".')
            print(f"Let's try again, {name}!")
            break

    else:
        print(f'Congratulations, {name}!')


