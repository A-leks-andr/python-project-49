from random import randint

import prompt


def get_progression(name):
    print('What number is missing in the progression?')
    for _ in range(3):
        start = randint(1, 15)
        end = randint(5, 10)
        diff = randint(3, 8)
        progression = [str(x * diff) for x in range(start, start + end)]
        selection = randint(0, len(progression) - 1)
        check = progression[selection]
        progression[selection] = '..'
        print(f'Question: {' '.join(progression)}')
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