# parrotList = ["not pinin", "no more", "bereft of life"]
#
# for state in parrotList:
#     print("this parrot is " + state)
#
# #
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
# #
# # number = even + odd
#
# # will not work
# # print(number.sort())
#
# # will sort the list
# # number.sort()
#
# # will create a new sorted list
# newNumbers = sorted(number)
#
# # lists that have the same elements but are in different orders are not equal
# if number == newNumbers:
#     print('1')
# else:
# #     print('2')
#
# list_1 = []
# list_2 = list()
#
# print('{}, {}'.format(list_1, list_2))
#
# print(list('The lists are equal'))

# this list is linked to the same point in memory as even
another_even = even

# This will create a new list not liked to even
another_even = list(even)

another_even.sort(reverse=True)
print(even)


numbers = [even, odd]

# prints the contents of numbers
for number_set in numbers:
    print(number_set)

    # prints the values of the list in numbers
    for value in number_set:
        print(value)
