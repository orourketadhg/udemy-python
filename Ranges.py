print(range(100))

myList = list(range(10))
print(myList)

# create list of 10000 odd elements
odd = range(1, 10000, 2)
# print list item 985
print(odd[985])

# multiplies step by 5: (2 * 5)  = 10
odd2 = odd[::5]
print(odd2)

# create list of numbers 0 - 9
smallDecimals = range(0, 10)

# print range object adding step to range
myRange = smallDecimals[::2]
print(myRange)


# print multiples of 3
i = iter(range(1, 11))

for j in range(3, 30, 3):
    print('3 * {} = {}'.format(next(i), j))

# both create list [0, 2, 4]
print(range(0, 5, 2) == range(0, 6, 2))

r = range(0, 100, 2)

for i in r[::-2]:
    print(i)

# runs through string in reverse
backString = 'dlrow olleh'
print(backString[::-1])