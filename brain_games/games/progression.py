from random import randint


def get_description():
    return "What number is missing in the progression?"


def generate_round():
    start = randint(1, 20)  # NOSONAR
    step = randint(1, 10)  # NOSONAR
    length = randint(5, 10)  # NOSONAR
    
    progression = [start + i * step for i in range(length)]
    
    hidden_index = randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    
    question = ' '.join(map(str, progression))
    return question, str(correct_answer)
