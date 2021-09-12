
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

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


country_list = country_file('countries.txt')


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


capital_list = capital_file('capitals.txt')


def ask_name():
    '''
    The function gets the name of the player and
    welcomes the player to the game.
    '''
    player_name = input('Please enter your name.\n')
    print(f'Welcome to the game {player_name}!')
    return player_name


ask_name()


def play_game():
    '''
    The function runs the game, asks the player a question,
    validates the response of the player and returns
    the score of the player.
    '''
    country_list
    capital_list
    player_score = 0
    while True:

        random_index = randint(0, 9)
        country = country_list[random_index]
        country_index = country_list.index(country)
        print(f'What is the capital city of {country}?')

        def validate_response():
            while True:
                response = input(
                    'Please enter city name. For example Asmara, Dublin.\n')
                answer = capwords(response)

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

        for i in range(len(capital_list)):
            if i == country_index and capital_list[i] == player_answer:
                print(f'The capital of {country} is: {capital_list[i]}')
                print('Well done!')
                player_score += 1
                break

        else:
            print('You missed this time')
            print('Hint: Next time check your spelling')

        play = input('To continue playing enter: y or n to quit\n')
        if play.lower() == 'y':
            continue

        return player_score


score = play_game()
print(score)
