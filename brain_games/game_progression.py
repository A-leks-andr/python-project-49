from random import randint

from brain_games.q_and_a import quest_answer


def get_progression(name):
    print("What number is missing in the progression?")
    for _ in range(3):
        start = randint(1, 15)
        end = randint(5, 10)
        diff = randint(3, 8)
        progression = [str(x * diff) for x in range(start, start + end)]
        selection = randint(0, len(progression) - 1)
        check = progression[selection]
        progression[selection] = ".."
        quest = f"Question: {' '.join(progression)}"
        answer = quest_answer(quest, check, name)
        if answer == "mistake":
            break

    else:
        print(f"Congratulations, {name}!")
