import prompt


def quest_answer(quest, check, name):
    print(quest)
    answer = prompt.string("Your answer: ")
    if answer == check:
        print("Correct!")

    else:
        print(f'"{answer}" is wrong answer ;(. Correct answer was "{check}".')
        print(f"Let's try again, {name}!")
        return "mistake"
