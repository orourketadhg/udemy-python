myList = ['a', 'b', 'c', 'd']

# # not efficient in terms of memory and runtime
# newString = ''
# for c in myList:
#     newString += c + ", "
#
# print(newString)

# joins a list together and returns a string
# each element is separated by a ', '
newString = ", ".join(myList)

print(newString)