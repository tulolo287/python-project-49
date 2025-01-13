import random

import prompt

from brain_games.cli import welcome_user

MAX_CORRECT_ANSWERS = 3
MAX_NUMBER_RANGE = 100


def main():
    user_name = welcome_user()
    game(user_name)


def game(user_name):
    correct_answers = MAX_CORRECT_ANSWERS
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while correct_answers:
        random_number = get_random_number()
        print(f"Question: {random_number}")
        answer = prompt.string("Your answer: ")
        good_answer = get_good_answer(random_number)

        if answer == good_answer:
            correct_answers -= 1
            print("Correct!")
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{good_answer}'.\n"
                f"Let's try again, {user_name}!"
            )
            correct_answers = MAX_CORRECT_ANSWERS

    print(f"Congratulations, {user_name}!")


def get_good_answer(random_number):
    if is_even(random_number):
        return "yes"
    return "no"


def is_even(number):
    return number % 2 == 0


def get_random_number():
    return random.randint(0, MAX_NUMBER_RANGE)
