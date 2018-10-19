import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}".format(highest))
guess = int(input('>>>'))

while guess != answer:
    if guess == 0:
        print('exiting')
        break
    else:
        if guess > answer:
            print('guess something lower')
        else:
            print('guess something higher')
    guess = int(input('>>>'))
else:
    print('you got it, the number was {}'.format(answer))