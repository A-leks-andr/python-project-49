import prompt


def quest_answer(func):
    print("Welcome to the Brain Games!")
    nick = prompt.string("May I have your name? ")
    print(f"Hello, {nick}")
    count = 0
    for _ in range(3):
        greet, quest, check = func()
        if count == 0:
            print(greet)
            count = 1
        print(quest)
        answer = prompt.string("Your answer: ")
        if answer == check:
            print("Correct!")

        else:
            print(
                f'"{answer}" is wrong answer ;(. Correct answer was "{check}".'
            )
            print(f"Let's try again, {nick}!")
            break
    else:
        print(f"Congratulations, {nick}")
