import random

from brain_games.scripts.games.brain_games import welcome_user
from brain_games.scripts.main import game

MAX_CORRECT_ANSWERS = 3
MAX_NUMBER_RANGE = 10


def main():
    user_name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    correct_answers = 0

    while correct_answers < MAX_CORRECT_ANSWERS:
        first_number = random.randint(1, MAX_NUMBER_RANGE)
        second_number = random.randint(1, MAX_NUMBER_RANGE)

        good_answer = get_correct_answer(first_number, second_number)
        question = f"Question: {first_number} {second_number}"
        correct_answers = game(
            user_name, question, good_answer, correct_answers
        )
    print(f"Congratulations, {user_name}!")


def get_correct_answer(first_number, second_number):
    if first_number == 0 or second_number == 0:
        return str(max(first_number, second_number))
    return get_correct_answer(second_number, first_number % second_number)
