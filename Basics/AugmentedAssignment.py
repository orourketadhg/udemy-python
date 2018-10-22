number = '9,223,372,036,854,775,907'
cleanedNumber = ''

# alternative way to add a number to itself
for i in range(0, len(number)):
    if number[i] in '0123456789':
        # Augmented assignment is +=, in C it is ++ to increment
        cleanedNumber += number[i]

# cast cleanNumber as int to newNumber
newNumber = int(cleanedNumber)

print(newNumber)

x = 24

# short way to get 24 mod 12
x %= 12

print(x)

greetings = 'good'
greetings += 'morning\n'

# multiply by 5
greetings *= 5

print(greetings)
