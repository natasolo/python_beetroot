# Write a program that generates a random number between 1 and 10 and let’s
# the user guess what number was generated. The result should be sent back
# to the user via a print statement.

import random
while True:
    a = random.randint(1,10)
    c = int(input("Please, input your number: "))
    if c != a:
        print('The number should be: ', a)
        continue
    else:
        print('You are right')
        break

# Write a program that takes your name as input, and then your age as input
# and greets you with the following:
# “Hello <name>, on your next birthday you’ll be <age+1> years”

user_name = (input("Enter your name: "))
user_age = int(input("Enter your age: "))
user_age += 1
print(f'Hello {user_name}, on your next birthday you’ll be {str(user_age)} years')