age = 24

# casts age to a string in the print()
print('my age is ' + str(age) + 'years')

# replaces {X} with the data in .format()
print('my age is {0}'.format(age))

# goes in order of .format()'s arguments
print('my age is {0} {1}'.format(age, 'years old'))

# will automatically increment the {X} for each item in the format()
print('my age is {} {}'.format(age, 'years old'))

# % [data_type] is out of date in python DO NOT USE!!!

for i in range(1, 12):
    # {0:2} how many spaces are available in console for the data
    print('no. {0:2} squared is {0:4} and cubed is {2:4}'.format(i, i ** 2, i ** 3))

for i in range(1, 12):
    # right hand justified
    print('no. {0:2} squared is {0:>4} and cubed is {2:>4}'.format(i, i ** 2, i ** 3))

for i in range(1, 12):
    # left hand justified
    print('no. {0:2} squared is {0:<4} and cubed is {2:<4}'.format(i, i ** 2, i ** 3))
