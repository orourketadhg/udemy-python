# problem occuring

import pytz
import datetime

country = 'Europe/Paris'

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)

print("time in Paris: {} ".format(country))
