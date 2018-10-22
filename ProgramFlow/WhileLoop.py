# for i in range(10):
#     print(i)
#
# i = 11
# while i < 10:
#     print(i)
#     i += 1
#
# availableExits = ['North', 'East', 'South', 'West']
#
# chosenExit = ''
#
# while chosenExit not in availableExits:
#     chosenExit = input('>>>')
#     if chosenExit == 'exit':
#         print('exiting')
#         break
# else:
#     print('you exited')
import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}".format(highest))
guess = int(input('>>>'))
if guess != answer:
    if guess < answer:
        print('please guess higher')
    else:
        print('please guess lower')
    guess = int(input('>>>'))
    if guess == answer:
        print('you got it')
    else:
        print('you didnt get it')
else:
    print('you got it first time')
