# Challenge

# Write a small program to display information on the
# four clocks whose functions we have looked at:
# i.e time(), perf_counter(), monotonic() and process_time().
#
# use the documentation for the get_clock_info() function
# to work out how to call it for each of the clocks.

import time

# take start time
input('Start recording time')

runTimeStart = time.time()
perfTimeStart = time.perf_counter()
monoTimeStart = time.monotonic()

# take end time
input('End recording time')

runTimeEnd = time.time()
perfTimeEnd = time.perf_counter()
monoTimeEnd = time.monotonic()

# print time() info
print('Run time using time(): ')
print(runTimeEnd - runTimeStart)
print(time.get_clock_info('time'))

print()

# print perf_counter() info
print('performance time using perf_counter: ')
print(perfTimeEnd - perfTimeStart)
print(time.get_clock_info('perf_counter'))

print()

# print monotonic() info
print('monotonic time using monotonic(): ')
print(monoTimeEnd - monoTimeStart)
print(time.get_clock_info('monotonic'))

print()

# time to run this process
print('Run time using process_time: ')
print(time.process_time())
print(time.get_clock_info('process_time'))