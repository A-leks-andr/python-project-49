from random import randint

from brain_games.q_and_a import quest_answer


def which_evens(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        number = randint(1, 50)
        if number % 2 == 0:
            check = "yes"
        else:
            check = "no"

        quest = f"Question:  {number}"
        answer = quest_answer(quest, check, name)
        if answer == "mistake":
            break

    else:
        print(f"Congratulations, {name}!")
