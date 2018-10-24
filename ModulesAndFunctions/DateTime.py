# import time
#
# # print epoch
# print("epoch is {}".format(time.strftime('%c', time.gmtime(0))))
#
# # print current time
# print("current timezone is {} with an offset of {}".format(time.tzname[0], time.timezone))
#
# # checks if current time has daylight savings in effect
# if time.daylight != 0:
#     print("\t Daylight savings is in effect")
#     # daylight savings
#     print(time.tzname[1])
# else:
#     print("\t Daylight savings is not in effect")
#     # no daylight savings
#     print(time.tzname[0])
#
# # print date and time in string format
# print(time.strftime('%d-%m-%Y %H:%M:%S'))

import datetime

# prints current data
# in UTC + 0 there will be no difference except for runtime allowance
print(datetime.datetime.today())
print(datetime.datetime.utcnow())
print(datetime.datetime.now())

