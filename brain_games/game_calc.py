import operator
from random import randint


def get_calc():
    act = iter([operator.add, operator.sub, operator.mul])
    sim = iter(["+", "-", "*"])
    greet = "What is the result of the expression?"
    a = randint(1, 15)
    b = randint(1, 15)
    check = str(next(act)(a, b))
    quest = f"Question: {a} {next(sim)} {b}"
    return greet, quest, check
