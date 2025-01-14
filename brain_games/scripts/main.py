import prompt


def game(user_name, question, good_answer, correct_answers):

    print(question)

    answer = prompt.string("Your answer: ")
    if answer == good_answer:
        correct_answers += 1
        print("Correct!")
    else:
        correct_answers = 0
        print(
            f"'{answer}' is wrong answer ;(. Correct answer was '{good_answer}'.\n"
            f"Let's try again, {user_name}!"
        )
    return correct_answers
