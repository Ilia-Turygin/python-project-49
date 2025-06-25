from prompt import string
from random import randint, choice
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print("What is the result of the expression?")
    correct_answers = 0

    operations = ['+', '-', '*']
    
    while correct_answers < 3:
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        operation = choice(operations)
        
        if operation == '+':
            correct_answer = num1 + num2
        elif operation == '-':
            correct_answer = num1 - num2
        else:
            correct_answer = num1 * num2
        
        print(f'Question: {num1} {operation} {num2}')
        answer = string('Your answer: ')
        
        if int(answer) == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}!")
            break
    
    if correct_answers == 3:
        print(f'Congratulations, {name}!')