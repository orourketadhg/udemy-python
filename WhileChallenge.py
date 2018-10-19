# Challenge

# imports a library into the file
import random

highest = 10
# generates a random number between 1 and highest(10)
answer = random.randint(1, highest)

# user input
print("Please guess a number between 1 and {}".format(highest))
guess = int(input('>>>'))

while guess != answer:
    # if guess is 0 exit
    if guess == 0:
        print('exiting')
        break
    else:
        # if guess is too low
        if guess > answer:
            print('guess something lower')
        else:
            # if guess is too high
            print('guess something higher')
    # next guess
    guess = int(input('>>>'))
else:
    # correct guess recieved
    print('you got it, the number was {}'.format(answer))