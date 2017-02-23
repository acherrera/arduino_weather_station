"""
Created by Anthony Herrera to analyze Arduino weather station data.

"""
# TODO convert timestamp to UNIX time or a useable date time stamp for graphing

# Time comes in form %04d%02d%02d_%02d%02d%02d - Because I made it that way.
# Data is of form: Time, Temperature, Pressure, Relative Humidity.

import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import datetime

filePath = 'datasets/20170223_091400.txt'

data = []
with open(filePath) as f:
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


# Time to get plotting
fig = plt.figure() # This is the 'canvas' of the plot. Used later for changes

# Subplot 1
ax1 = plt.subplot(3, 1, 1)
plt.plot(time, temp)
plt.ylabel('Temperature')
plt.setp(ax1.get_xticklabels(), visible=False)

# Subplot 2
ax2 = plt.subplot(3, 1, 2)
plt.plot(time, pressure)
plt.ylabel('Pressure')
plt.setp(ax2.get_xticklabels(), visible=False)

# Subplot 3
ax3 = plt.subplot(3, 1, 3)
plt.plot(time, rel_hum)
plt.xlabel('time')
plt.ylabel('RH')

# Adjust the x-axis to look nice
fig.suptitle('Sensor Data: {}'.format(filePath.split('.')[0].split('/')[1]))

xfmt = mdate.DateFormatter('%H:%M') # this is what make the x-axis format correctly
ax3.xaxis.set_major_formatter(xfmt)
fig.autofmt_xdate() # This works alright

# fig.tight_layout()

plt.savefig("{}.png".format(filePath.split('.')[0]))
plt.show()
