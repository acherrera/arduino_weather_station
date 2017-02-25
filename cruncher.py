"""
Created by Anthony Herrera to analyze Arduino weather station data.

"""
# TODO put lines in graph where sensor was messed with, potentially skewing results
# TODO need an input method to select starting time and minute. Maybe not second.
# TODO add temperature conversion availability. Need to update graph axis labels
# TODO modulurize

# Time comes in form %04d%02d%02d_%02d%02d%02d - Because I made it that way.
# Data is of form: Time, Temperature, Pressure, Relative Humidity.

import datetime
import time

import matplotlib.dates as mdate
import matplotlib.pyplot as plt
import numpy as np

from lib.helpers import get_start

filePath = 'datasets/20170225_083900_Bedroom_Overnight.TXT'

with open(filePath) as f:
    data = f.readlines()

time_list = []
temp = []
pressure = []
rel_hum = []

# Sea Level Correction
elevation = 288  # m
gravity = 9.80665  # m/s^2
R = 287


def to_Kelvin(T):
    return T + 273.15


# Better implement this, see temp.py. Make all of this it's own function that returns datetime object. Till 71
current_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S').split('-')
year_current = int(current_time[0])
month_current = int(current_time[1])
day_current = int(current_time[2])
hour_current = int(current_time[3])
minute_current = int(current_time[4])


year_start = get_start("Year", year_current)
month_start = get_start("Month", month_current)
day_start = get_start("Day", day_current)
hour_start = get_start("Hour", hour_current)
minute_start = get_start("Minute", minute_current)
second_start = 0

# This will check if the current time and the start time match. Overwrites current time - whatever
current_time = datetime.datetime(year_current, month_current, day_current, hour_current,
                                 minute_current, 0)

start_time = datetime.datetime(year_start, month_start, day_start, hour_start,
                               minute_start, second_start)

# They the two times do match, set start to time way back. Could also use a boolean and check that
if current_time == start_time:
    print("Graphing All Data")
    start_time = datetime.datetime(2000, 1, 1, 1, 1, 1)

print("Start time is: {}".format(start_time))

# Possible make this it's own thing too
for line in data:

    if line.startswith('#'):  # test if this work. Add comment to file
        pass
    else:
        time_data = str(line.split(',')[0])
        year = int(time_data[0:4])
        month = int(time_data[4:6])
        day = int(time_data[6:8])
        hour = int(time_data[9:11])
        minute = int(time_data[11:13])
        second = int(time_data[13:15])

        in_time = datetime.datetime(year, month, day, hour, minute, second)
        # These are datetime object comparison
        if in_time > start_time:
            time_list.append(in_time)
            temperature = float(line.split(',')[1])
            temp.append(temperature)
            input_pressure = float(line.split(',')[2])
            corrected_pressure = input_pressure * np.exp((elevation * gravity) / (R * to_Kelvin(temperature)))
            pressure.append(corrected_pressure)
            rel_hum.append(float(line.split(',')[3]))

if len(time_list) < 3:
    print("Please check starting times\nProgram Exiting")
    quit()

# Make plotting its own function also
fig = plt.figure()  # This is the 'canvas' of the plot. Used later for changes

# Subplot 1
ax1 = plt.subplot(3, 1, 1)
plt.plot(time_list, temp)
plt.ylabel('Temperature (C)')
plt.setp(ax1.get_xticklabels(), visible=False)

# Subplot 2
ax2 = plt.subplot(3, 1, 2)
plt.plot(time_list, pressure)
plt.ylabel('Pressure (hPa)')
plt.setp(ax2.get_xticklabels(), visible=False)

# Subplot 3
ax3 = plt.subplot(3, 1, 3)
plt.plot(time_list, rel_hum)
plt.xlabel('Time')
plt.ylabel('RH (%)')

# use to add text to figure image
# fig.text(0, 0, 'Note the spikes around 1am appear to be from hail hitting the box. Not likely to be\n'
# 'due to wind as the inconsistency coincides with reported hail')

# Adjust the x-axis to look nice
fig.suptitle('Sensor Data: {}'.format(filePath.split('.')[0].split('/')[1]))

xfmt = mdate.DateFormatter('%H:%M')  # this is what make the x-axis format correctly
ax3.xaxis.set_major_formatter(xfmt)
fig.autofmt_xdate()  # This works alright

# fig.tight_layout()

plt.savefig("{}.png".format(filePath.split('.')[0]))
plt.show()

print(pressure[-1])
