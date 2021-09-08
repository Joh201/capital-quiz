
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


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


