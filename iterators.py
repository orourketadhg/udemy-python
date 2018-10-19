# string = "1234567890"
#
# # for char in string:
# #     print(char)
#
# my_iterator = iter(string)
#
# print(my_iterator)
#
# print(next(my_iterator))
# print(next(my_iterator))
#
#
# for char in string:
#     print(char)
#
# # what is happening in the background of the for loop
# for char in iter(string):
#     print(char)

# Create a list of items (you may use either strings or numbers in the list)
# then create an iterator using the iter() function.
# use a for loop "n" limes, where n is the number of items in your list
# each time round the loop, use next() on your list to print the next item.
# hint: use the len()= function rather than counting the number of items in the list.

newList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

i = iter(newList)

for num in range(0, len(newList)):
    print(next(i))
