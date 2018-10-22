# name = input('name: ')
age = int(input('age: '))

# # if age id greater than
# if age > 18:
#     print(name + ', you are old enough to drink!')
# # age is older than 18
# elif age < 18:
#     print(name + ', you are too young to drink')
# # age == 18
# else:
#     print('you {} are just the right age to start drinking'.format(age))

# works the same as and operator
if 18 <= age <= 100:
    print('you are alive and can drink')
elif age > 18 or age > 100:
    print('you cannot vote or you are likely dead')

