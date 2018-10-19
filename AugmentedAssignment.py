number = '9,223,372,036,854,775,907'
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        # Augmented assignment is +=, in C it is ++ to increment
        cleanedNumber += number[i]

newNumber = int(cleanedNumber)

print(newNumber)

x = 24

x %= 12

print(x)

greetings = 'good'
greetings += 'morning\n'

greetings *= 5

print(greetings)
