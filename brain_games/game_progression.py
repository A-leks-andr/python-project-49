from random import randint


def get_progression():
    greet = "What number is missing in the progression?"
    start = randint(1, 15)
    end = randint(5, 10)
    diff = randint(3, 8)
    progression = [str(x * diff) for x in range(start, start + end)]
    selection = randint(0, len(progression) - 1)
    check = progression[selection]
    progression[selection] = ".."
    quest = f"Question: {' '.join(progression)}"
    return greet, quest, check
