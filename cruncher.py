"""
Created by Anthony Herrera to analyze Arduino weather station data.

"""
# TODO convert timestamp to UNIX time or a useable date time stamp for graphing

# Time comes in form %04d%02d%02d_%02d%02d%02d - Because I made it that way.
# Data is of form: Time, Temperature, Pressure, Relative Humidity.

import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import datetime

data = []
with open('20170223_091400.txt.TXT') as f:
    data = f.readlines()

time = []
temp = []
pressure = []
rel_hum = []

start_index = 0

for line in data:

    time_data = str(line.split(',')[0])
    year = int(time_data[0:4])
    month = int(time_data[4:6])
    day = int(time_data[6:8])
    hour = int(time_data[9:11])
    minute = int(time_data[11:13])
    second = int(time_data[13:15])
    time.append(datetime.datetime(year,month,day,hour,minute, second))

    temp.append(float(line.split(',')[1]))
    pressure.append(float(line.split(',')[2]))
    rel_hum.append(float(line.split(',')[3]))

x = [i for i in range(len(temp))]

fig, ax1 = plt.subplots()
ax1.plot(time, temp, 'b-')
ax1.set_xlabel('time (not really)')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('Temperature', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(time, rel_hum, 'r-')
ax2.set_ylabel('Relative Humidity', color='r')
ax2.tick_params('y', colors='r')


# This might as well be voodoo, but it works well enough.
xfmt = mdate.DateFormatter('%H:%M:%S')
ax1.xaxis.set_major_formatter(xfmt)
fig.autofmt_xdate() # This works alright



fig.tight_layout()
plt.show()

plt.show()


""" Dumb Anthony way of plotting data
plt.subplot(2, 1 ,1)
plt.plot(x, temp)
plt.xlabel('Time - not really')
plt.ylabel('Temp')

plt.subplot(2, 1 ,2)
plt.plot(x, pressure)
plt.xlabel('Time - not really')
plt.ylabel('Pressure')
"""