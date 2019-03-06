from typing import Dict


# Create a simple function called favourite_movie, which takes a string
# containing the name of your favourite movie. The function should then
# print “My favourite movie is name”.
#
def favourite_movie(movie_name: str):
    print('My favourite movie is ' + movie_name)


m = input('What is your favourite movie? ')
favourite_movie(m)


# Create a function called make_country, which takes in a country’s name and
# capital as parameters. Then create a dictionary from those parameters,
# with ‘name’ and ‘capital’ as keys. Make the function print out the values
# of the dictionary to make sure that it works as intended.
# from typing import Dict
#
#
def make_country(country: str, capital: str) -> Dict:
    result = {
        'country': country,
        'capital': capital
    }
    print(result)
    return result


country_cap = make_country(country='Ukraine', capital='Kiev')


# Create a function called make_operation, which takes in a simple
# arithmetic operator as a first parameter (to keep things simple let it
# only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only
# numbers) as second parameter. Then return the sum or product of all the
# numbers in the arbitrary parameter.
def make_operation(arithmetic_operator: str, *args: int) -> int:
    result = args[0]
    for number in args[1:]:
        if arithmetic_operator == '+':
            result += number
        elif arithmetic_operator == '-':
            result -= number
        elif arithmetic_operator == '*':
            result *= number
        else:
            print('Use other operator')
            break
    return result


first = make_operation('+', 7, 7, 2)
second = make_operation('-', 5, 5, -10, -20)
third = make_operation('*', 7, 6)
print(first, second, third)
