import datetime
import time

# Testing better implementation of the current time function. This works well.
current_time = datetime.datetime.fromtimestamp(time.time())

year = current_time.year
month = current_time.month
day = current_time.day

print(type(day))
print(day)
