# accessing and using system time
import time
import random

# all return to a struct

# start of the sm time - epoch - 1/1/1970 - works in UTC
print(time.gmtime(0))
# data relating to local time based on computer time and date
print(time.localtime())
# prints the number of seconds since epoch
# can have problems with day light savings and system time drift
print(time.time())

time_here = time.localtime()

# prints the current local time structure
print(time_here)

# prints the data structures data
print('Year: ',  time_here[0])
print('Month: ',time_here[1])
print('Day: ', time_here[2])
print('Hour: ', time_here[3])
print('Minute: ', time_here[4])

input('random wait time')

wait_time = random.randint(1, 5)

# wait a random amount of time between 1 and 5 seconds
time.sleep(wait_time)

# take a start time
start_time = time.time()

# wait until enter key hit
input('HIT ME')

# take end time
end_time = time.time()

# strftime: stringFromTime
# prints the time in 00:00:00 in reference to localtime
print(time.strftime("%X", time.localtime(start_time)))

print(end_time)

# print time difference
print(end_time - start_time)

# perf_counter()
# records the preform time
perf = time.perf_counter()
print(perf)

# monotonic()
# similar to perf_counter
# adjustments to system clock and day light savings will not affect this

mono = time.monotonic()
print(perf)

# process_time()
# returns time that a process takes rather than system time
print(time.process_time())