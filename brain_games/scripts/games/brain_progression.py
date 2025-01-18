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
        progression_number = random.randint(1, 100)
        unknown_number_i = random.randint(1, MAX_NUMBER_RANGE - 1)
        progression_gap = random.randint(1, MAX_NUMBER_RANGE)
        progression = []
        good_answer = None
        
        for i in range(MAX_NUMBER_RANGE):
            if unknown_number_i == i:
                good_answer = str(progression_number)
                progression.append("...")
            else:
                progression.append(str(progression_number))
            progression_number += progression_gap

        progression_str = ", ".join(progression)

        question = f"Question: {progression_str}"
        correct_answers = game(
            user_name, question, good_answer, correct_answers
        )
    print(f"Congratulations, {user_name}!")

