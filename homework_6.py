# Make a program that generates a list that has all squared values of integers
# from 1 to 100, i.e., like this: [1, 4, 9, 16, 25, 36, …, 10000]

a = list()
for element in range(1, 101):
    a.append(element ** 2)
print(a)

# Make a program that prompts the user to input the name of a car, the program
# should save the input in a list and ask for another, and then another,
# until the user inputs ‘q’, then the program should stop and the list of
# cars that was produced should be printed.

list_of_inputs = []

while True:
    user_input = input('Enter the name of a car: ')
    if user_input == 'q':
        break
    list_of_inputs.append(user_input)

print(list_of_inputs)

# Start of with any list containing at least 10 elements, then print all elements
# in reverse order.

a = [1, 8, 4, 0, 45, 98, 67, 98, 10, 48]
print(sorted(a, reverse=True))