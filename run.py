
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from random import randint

def country_file(file):
    '''
    The function reads the file containing
    the country list
    '''

    f = open(file, 'r')
    countries = f.readlines()
    f.close()
    country_name = []
    for country in countries:
        country_name.append(country.replace('\n', ''))
    return country_name  
      

print(country_file('countries.txt'))


def capital_file(file):
    '''
    The function reads the file containing
    the capital city list
    '''

    f = open(file, 'r')
    capital_cities = f.readlines()
    f.close()
    capital_name = []
    for capital in capital_cities:
        capital_name.append(capital.replace('\n', ''))    
    return capital_name  
    

print(capital_file('capitals.txt'))


def play_game():
    '''
    The function runs the game and asks the player to
    input their response. 

    '''
    player_name = input('Pleae enter your name.\n')
    print(f'Welcome to the game {player_name}!')
    country_list = country_file('countries.txt')
    capital_list = capital_file('capitals.txt')
    random_index = randint(0, 4)
    
    print(f'What is the capital city of {country_list[random_index]}?')
    response = input('Please enter city name. For example Asmara, Stockholm.\n')
    print(response)
    


    
    
play_game()