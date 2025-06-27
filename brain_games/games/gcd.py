from random import randint


def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def get_description():
    return 'Find the greatest common divisor of given numbers.'


def generate_round():
    num1 = randint(1, 10)
    num2 = randint(1, 10)
        
    question = f'{num1} {num2}'
    correct_answer = calculate_gcd(num1, num2)
    
    return question, str(correct_answer)

    