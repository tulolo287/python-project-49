import random

from brain_games.cli import welcome_user
from brain_games.scripts.main import game

MAX_CORRECT_ANSWERS = 3
MAX_NUMBER_RANGE = 10
SIGNS_COUNT = 3


def main():
    user_name = welcome_user()
    print("What is the result of the expression?")

    signs = ["+", "-", "*", "/"]
    correct_answers = 0

    while correct_answers < MAX_CORRECT_ANSWERS:
        first_number = random.randint(0, MAX_NUMBER_RANGE)
        second_number = random.randint(0, MAX_NUMBER_RANGE)
        sign = signs[random.randint(0, SIGNS_COUNT - 1)]

        good_answer = get_correct_answer(first_number, second_number, sign)
        question = f"Question: {first_number} {sign} {second_number}"
        correct_answers = game(
            user_name, question, good_answer, correct_answers
        )
    print(f"Congratulations, {user_name}!")


def get_correct_answer(first_number, second_number, sign):
    match sign:
        case "+":
            return str(int(first_number + second_number))
        case "-":
            return str(int(first_number - second_number))
        case "*":
            return str(int(first_number * second_number))
        case "/":
            return str(int(first_number / second_number))
