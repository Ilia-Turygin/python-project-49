import prompt
from random import randint


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    name = prompt.string('Answer "yes" if the number is even, otherwise answer "no".')


