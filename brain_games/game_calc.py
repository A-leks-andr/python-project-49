import operator
import prompt
from random import randint
from brain_games.q_and_a import quest_answer


def get_calc(name):
    act = [operator.add, operator.sub, operator.mul]
    sim = ["+", "-", "*"]
    print("What is the result of the expression?")
    for i in range(3):
        a = randint(1, 15)
        b = randint(1, 15)
        check = str(act[i](a, b))
        quest = f"Question: {a} {sim[i]} {b}"
        answer = quest_answer(quest, check, name)
        if answer == "mistake":
            break

    else:
        print(f"Congratulations, {name}!")
