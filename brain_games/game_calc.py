import operator
from random import randint

import prompt


def get_calc(name):

    act = [operator.add, operator.sub, operator.mul]
    sim = ['+', '-', '*']
    print('What is the result of the expression?')
    for i in range(3):

        a = randint(1, 15)
        b = randint(1, 15)
        check = str(act[i](a, b))
        print(f'Question: {a} {sim[i]} {b}')
        answer = prompt.string('Your answer: ')

        if answer == check:
            print('Correct!')

        else:
            print(f'"{answer}" is wrong answer ;(.'
                   'Correct answer was "{check}".')
            print(f"Let's try again, {name}")
            break

    else:
        print(f'Congratulations, {name}')

