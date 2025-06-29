from random import choice, randint


def get_description():
    return 'What is the result of the expression?'


def generate_round():

    operations = ['+', '-', '*']

    num1 = randint(1, 10) # NOSONAR
    num2 = randint(1, 10) # NOSONAR
    operation = choice(operations) # NOSONAR

    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
        
    question = f'{num1} {operation} {num2}'

    return question, str(correct_answer)
