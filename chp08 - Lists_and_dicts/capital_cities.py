import random
status = 'Correct'
state = ''
entry = ''
capitals = {
    'NSW': 'Sydney',
    'Victoria': 'Melbourne',
    'Queensland': 'Brisbane',
    'Western Australia': 'Perth',
    'South Australia': 'Adelaide',
    'ACT': 'Canberra',
    'Tasmania': 'Hobart',
    'Northern Territory': 'Darwin',
    }

while status != 'Goodbye.':
    if status == 'Correct':
        state = random.choice(list(capitals.keys()))
        print(f'What is the capital of {state}?')

    entry = input('Enter your answer or type "exit": ')

    if entry.lower() == 'exit':
        status = 'Goodbye.'
    elif entry.lower() == capitals[state].lower():
        status = 'Correct'
    else:
        status = 'Incorrect'

    print(status)
