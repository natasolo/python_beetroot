# Make a program that given a whole sentence (a string) will make a dict
# containing all unique words as keys and the number of occurrences as
# values.
user_input = str(input('Please, enter your favorite quote:  ')).split()
user_dict = {word: user_input.count(word) for word in user_input}
print(user_dict)

# Consider the following list: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Now, make a program (no longer than one line) that makes a new list
# containing all the values in a
# but no even numbers.

list_1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list_2 = [number for number in list_1 if number % 2 != 0]
print(list_1, list_2)

# Use a list comprehension to make a list containing tuples (i, j) where i
# goes from 1 to 10 and j is corresponding i squared.


my_list = [(i, i**2) for i in range(1, 11)]
print(my_list)