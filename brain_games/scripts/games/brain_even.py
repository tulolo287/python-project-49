import random

from brain_games.cli import welcome_user
from brain_games.scripts.main import game

MAX_CORRECT_ANSWERS = 3
MAX_NUMBER_RANGE = 100


def main():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0
    while correct_answers < MAX_CORRECT_ANSWERS:
        random_number = get_random_number()
        good_answer = get_good_answer(random_number)
        question = f"Question: {random_number}"
        correct_answers = game(
            user_name, question, good_answer, correct_answers
        )
    print(f"Congratulations, {user_name}!")


def get_good_answer(random_number):
    if is_even(random_number):
        return "yes"
    return "no"


def is_even(number):
    return number % 2 == 0


def get_random_number():
    return random.randint(0, MAX_NUMBER_RANGE)
