from prompt import string

from random import randint
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    rules()
    correct_answers = 0

    while correct_answers < 3:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        answer = string('Your answer: ')

        if (random_number % 2 == 0 and answer == 'yes') or (random_number % 2 != 0 and answer == 'no'):
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was {'yes' if random_number % 2 == 0 else 'no'}.")
            print(f"Let's try again, {name}!")
            correct_answers = 0 

    print(f'Congratulations, {name}!')



def rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')

