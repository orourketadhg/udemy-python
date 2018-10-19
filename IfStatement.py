# name = input('name: ')
age = int(input('age: '))

# if age > 18:
#     print(name + ', you are old enough to drink!')
# elif age < 18:
#     print(name + ', you are too young to drink')
# else:
#     print('you {} are just the right age to start drinking'.format(age))

# if condition works the same as an and operator
if 18 <= age <= 100:
    print('you are alive and can drink')
elif age > 18 or age > 100:
    print('you cannot vote or you are likely dead')

