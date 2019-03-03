# Generate 2 lists of length 10 with random integers from 1 to 10, and make
# a third list containing the common integers between the 2 initial lists
# without any duplicates.
import random

a = [random.randrange(1, 10) for number in range(10)]
b = [random.randrange(1, 10) for number in range(10)]
print(a, b)
c = list(set(a).intersection(b))
print(c)

# Make a list that contains all integers from 1 to 100, then find all
# integers from the list that are divisible by 7 but not a multiple of 5 and
# store them in a separate list. Finally print the list.

a = [number for number in range(1, 100)]
b =[number for number in a if number % 7 == 0 and number % 5 != 0]
print(a)
print(b)