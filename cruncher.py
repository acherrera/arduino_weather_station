"""
Created by Anthony Herrera to analyze Arduino weather station data.

"""
# TODO put lines in graph where sensor was messed with, potentially skewing results

# Time comes in form %04d%02d%02d_%02d%02d%02d - Because I made it that way.
# Data is of form: Time, Temperature, Pressure, Relative Humidity.

import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import datetime
import numpy as np

filePath = 'datasets/Bathroom_fan_pressure_test.TXT'

data = []
with open(filePath) as f:
    data = f.readlines()

time = []
temp = []
pressure = []
rel_hum = []

# Sea Level Correction
elevation = 288 # m
gravity = 9.80665 #m/s^2
R = 287

def to_Kelin(T):
    return T + 273.15

start_hour = int(input("What is the starting hour? (e.g. '15') Zero for all times:"))
if start_hour > 24 or start_hour < 1:
    start_hour = 0

for line in data:


    time_data = str(line.split(',')[0])
    year = int(time_data[0:4])
    month = int(time_data[4:6])
    day = int(time_data[6:8])
    hour = int(time_data[9:11])
    minute = int(time_data[11:13])
    second = int(time_data[13:15])

    if hour >= start_hour:

        time.append(datetime.datetime(year,month,day,hour,minute, second))
        temperature = float(line.split(',')[1])
        temp.append(temperature)
        input_pressure = float(line.split(',')[2])
        corrected_pressure = input_pressure*np.exp((elevation*gravity)/(R*to_Kelin(temperature)))
        pressure.append(corrected_pressure)
        rel_hum.append(float(line.split(',')[3]))


# Time to get plotting
fig = plt.figure() # This is the 'canvas' of the plot. Used later for changes

# Subplot 1
ax1 = plt.subplot(3, 1, 1)
plt.plot(time, temp)
plt.ylabel('Temperature (C)')
plt.setp(ax1.get_xticklabels(), visible=False)

# Subplot 2
ax2 = plt.subplot(3, 1, 2)
plt.plot(time, pressure)
plt.ylabel('Pressure (hPa)')
plt.setp(ax2.get_xticklabels(), visible=False)


# Subplot 3
ax3 = plt.subplot(3, 1, 3)
plt.plot(time, rel_hum)
plt.xlabel('Time')
plt.ylabel('RH (%)')

# use to add text to figure image
# fig.text(0, 0, 'Note the spikes around 1am appear to be from hail hitting the box. Not likely to be\n'
             #'due to wind as the inconsistency coincides with reported hail')

# Adjust the x-axis to look nice
fig.suptitle('Sensor Data: {}'.format(filePath.split('.')[0].split('/')[1]))

xfmt = mdate.DateFormatter('%H:%M') # this is what make the x-axis format correctly
ax3.xaxis.set_major_formatter(xfmt)
fig.autofmt_xdate() # This works alright

#fig.tight_layout()

plt.savefig("{}.png".format(filePath.split('.')[0]))
plt.show()

print(pressure[-1])