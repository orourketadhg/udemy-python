# Challenge

# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18 - 30 holiday (they must
# be over 18 and under 30)
# if they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry

name = input('Enter name: ')
age = int(input('Enter age: '))

if 18 <= age <= 30:
    print('Welcome to the holiday, {}'.format(name))
else:
    print('Sorry {}, you are not the right age to go on the holiday'.format(name))
