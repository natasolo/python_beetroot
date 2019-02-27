# Make a program that checks if a string is on the right format for a phone
# number. The program should check that the string contains only numerical
# characters and is only 10 characters long. Print a suitable message depending
# on the outcome of the string evaluation.
user_input = (input("Enter phone number: "))
if (user_input .isdigit()) and len(user_input) <= 10:
    print('This is a valid format')
else:
    print('This is not a valid format')

# Write a program that asks the answer for a mathematical expression, checks
# whether the user is right or wrong, and then responds with a message
# accordingly.
print("45 - 10 = ?")
user_input = input("Enter your choice: ")
if user_input.isdigit():
    number = int(user_input)
    if number == 35:
        print("Great, you're a genius!")
    else:
        print("Try harder next time...")
else:
   print("This a math quizz, think about it (^_^) ")

# Write a program that has a variable with your name stored (in lowercase) and
# then asks for your name as input. The program should check if your input is
# equal to the stored name even if the given name has another case, e.g., if your
# input is “Anton” and the stored name is “anton” it should return True.

my_name = 'natalya'
my_input = input('Enter your name: ')
if my_input.lower() == my_name:
    print(True)
else:
    print(False)

