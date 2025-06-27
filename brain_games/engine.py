from prompt import string

from brain_games.cli import welcome_user


def run_game(game_description, generate_round):
    name = welcome_user()
    game_rules = game_description
    print(game_rules)
    
    correct_answers = 0
    
    while correct_answers < 3:
        question, correct_answer = generate_round()
        print(f'Question: {question}')
        user_answer = string('Your answer: ')
        
        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(." 
                f"Correct answer was {correct_answer}."
                )
            print(f"Let's try again, {name}!")
            return
    
    print(f'Congratulations, {name}!')
    
   
