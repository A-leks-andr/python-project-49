from random import randint


def which_evens():
    greet = 'Answer "yes" if the number is even, otherwise answer "no".'
    number = randint(1, 50)
    if number % 2 == 0:
        check = "yes"
    else:
        check = "no"
    quest = f"Question:  {number}"
    return greet, quest, check
