# for i in range(1, 20):
#     print(i)
#
# number = "9,223,372,036,836,854,775,807"
# for i in range(0, len(number)):
#     print(number[i])
#
number = "9,223,372,036,836,854,775,807"
# cleanedNumber = ''
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         # concatenates each number string together
#         cleanedNumber = cleanedNumber + number[i]
#
# # turns cleanedNumber into a int
# newNumber = int(cleanedNumber)
#
# print(newNumber)

cleanedNumber = ''

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print("the number is {}".format(newNumber))

for state in ["test", 'case']:
    print('{}'.format(state))

