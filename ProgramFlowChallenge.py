# Create a program that takes an IP address entered at the keyboard
# and prints out the number of segments it contains, and the length of each segment.
#
# An IP address consists of 4 numbers, separated from each other with a full stop. But
# your program should just count however many are entered
# Examples of the input you may get are:
#    127.0.0.1
#    .192.168.0.1
#    10.0.123456.255
#    172.16
#    255
#
# So your program should work even with invalid IP Addresses. We're just interested in the
# number of segments and how long each one is.
#
# Once you have a working program, here are some more suggestions for invalid input to test:
#    .123.45.678.91
#    123.4567.8.9.
#    123.156.289.10123456
#    10.10t.10.10
#    12.9.34.6.12.90
#    '' - that is, press enter without typing anything
#
# This challenge is intended to practise for loops and if/else statements, so although
# you could use other techniques (such as splitting the string up), that's not the
# approach we're looking for here.

# Initialisation
segment = 1
segLength = 0

# IP input
ipAddress = input('Enter IP: ')

# input empty
if ipAddress == '':
    print('This is an invalid IP address code: 1')

# last element in IP '.'
elif ipAddress[-1] in '.':
    print('This is an invalid IP address code: 2')

# first element in IP '.'
elif ipAddress[0] in '.':
    print('This is an invalid IP address code: 3')

# letter in IP
elif ipAddress in 'abcdefghijklmnopqrstuvwxyz' or ipAddress in 'abcdefghijklmnopqrstuvwxyz'.upper():
    print('This is an invalid IP address code: 4')

# IP too long
elif len(ipAddress) > 15:
    print('This is an invalid IP address code: 5')

# IP too short
elif len(ipAddress) < 7:
    print('This is an invalid IP address code: 6')

# correct IP format
else:
    for i in range(0, len(ipAddress)):
        # if current element a number
        if ipAddress[i] in '0123456789':
            segLength += 1
        # current element a '.', print and reset for next segment
        else:
            print('Segment {} has {} numbers\n'.format(segment, segLength))
            segLength = 0
            segment += 1

# print last segment data
print('Segment {} has {} numbers\n'.format(segment, segLength))
