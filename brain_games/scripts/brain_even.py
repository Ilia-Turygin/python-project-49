import prompt
from random import randint
from brain_games.cli import welcome_user


def main():
    welcome_user()
    name = prompt.string('Answer "yes" if the number is even, otherwise answer "no".')




