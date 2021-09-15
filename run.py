from random import randint
from string import capwords


def country_file(file):
    '''
    The function reads the file containing
    the country list.
    '''
    f = open(file, 'r')
    countries = f.readlines()
    f.close()
    country_name = []
    for country in countries:
        country_name.append(country.replace('\n', ''))
    return country_name


def capital_file(file):
    '''
    The function reads the file containing
    the capital city list.
    '''
    f = open(file, 'r')
    capital_cities = f.readlines()
    f.close()
    capital_name = []
    for capital in capital_cities:
        capital_name.append(capital.replace('\n', ''))
    return capital_name


def ask_name():
    '''
    The function gets the name of the player and
    welcomes the player to the game.
    '''
    player_name = input('Please enter your name.\n')
    print(f'***Welcome to the Capital City game {player_name}!***')
    return player_name


def handle_quit(user_input, score, questions_answered_count):
    '''
    The function allows the player to continue palying or
    to exit the game. It also reports the player's score.
    '''
    if user_input.lower() == 'y':
        return
    elif user_input.lower() == 'n':
        print(f'You score is {score} out of {questions_answered_count}')
        quit()
    else:
        play = input('please enter y or n.\n')
        handle_quit(play, score, questions_answered_count)


def generate_rand_int(data):
    '''
    The function generates random numbers which are used
    to get random questions, and it ensures questions
    are not repeated while the game is running.
    '''
    random_index = randint(0, 24)
    if random_index in data:
        return generate_rand_int(data)
    return random_index


def play_game():
    '''
    The function runs the game, asks the player a question,
    validates the response of the player and returns
    the score of the player.
    '''
    country_list = country_file('countries.txt')
    capital_list = capital_file('capitals.txt')

    player_score = 0
    question_answered_indexes = []

    ask_name()

    while True:

        random_index = generate_rand_int(question_answered_indexes)
        country = country_list[random_index]
        country_index = country_list.index(country)
        print(f'What is the capital city of {country}?')

        # This function validates the users input
        def validate_response():
            while True:
                response = input(
                    'Please enter city name. For example Asmara, Dublin.\n')
                answer = capwords(response)

        # This section was adapted and modified based on course material
                try:
                    if answer.isdigit():
                        raise TypeError('You entered a number!')
                    elif any(str.isdigit(i) for i in answer):
                        raise TypeError('You entered a name with number!')
                    else:
                        return answer
                except TypeError as e:
                    print(f'Invalid input. {e}')

        player_answer = validate_response()

        # This code adds the question to the list of asked questions
        question_answered_indexes.append(country_index)

        # This section checks if the player's response is correct
        if capital_list[country_index] == player_answer:
            capital = capital_list[country_index]
            print(f'The capital of {country} is: {capital}')
            print('Well done!')
            player_score += 1

        else:
            print('You missed this time')
            print('Hint: Next time check your spelling')

        # This section handles players decision at the end of the game
        if len(question_answered_indexes) == 25:
            question_count = len(question_answered_indexes)
            print(f'You score is {player_score} out of {question_count}')
            play = input('Game ended, press y to start again or n to quit:\n')
            handle_quit(play, player_score, len(question_answered_indexes))
            player_score = 0
            question_answered_indexes.clear()
        else:
            play = input('To continue playing enter: y or n to quit\n')
            handle_quit(play, player_score, len(question_answered_indexes))


play_game()
