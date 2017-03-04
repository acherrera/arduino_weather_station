"""
This file is just for testing functions and seeing what works -
"""
import datetime

import matplotlib.dates as mdate
import matplotlib.pyplot as plt

from modules.functions import get_start, get_data, data_start

filePath = 'datasets/weather_data/20170226_official_data.py'
lines_scanned = 40

with open(filePath) as f:
    # Gets top 20 lines to look for first non-comment line
    data = f.readlines()

newtop = []
for line in data:
    # Take out tops line if they are not a comment or blank
    if line.startswith('#') or line == '\n':
        pass
    else:
        newtop.append(line)

header = newtop.pop(0)

station = []
time = []
temperature = []
dew_point = []
rel_hum = []
dirct = []

Year = []
Month = []
Day = []
Hour = []
Minute = []

times = []


def data_adder(item, parent_list):
    if item == 'M':
        parent_list.append(None)
    else:
        parent_list.append(item)


for line in newtop:
    sample = line.split(',')  # Turns into list

    data_adder(sample[0], station)
    time = sample[1]  # this is indexing odd.
    print(time)
    data_adder(sample[2], temperature)
    data_adder(sample[3], dew_point)
    data_adder(sample[4], rel_hum)
    data_adder(sample[5], dirct)

    YMD = time.split(' ')[0].split('-')
    HM = time.split(' ')[1].split(':')
    Year = (int(YMD[0]))
    Month = (int(YMD[1]))
    Day = (int(YMD[2]))
    Hour = (int(HM[0]))
    Minute = (int(HM[1]))

    times.append(datetime.datetime(Year, Month, Day, Hour, Minute, 0))

plot_times = []
plot_variable = []

for i in range(len(temperature)):
    if temperature[i] is not None:
        plot_variable.append((float(temperature[i]) - 32) / 1.8)
        plot_times.append(times[i])

the_file = 'datasets/weather_data/20170226_000000_morning_weather.TXT'

lines_to_scan = 40  # lines to scan for the first non-comment line

data_start = data_start(the_file, lines_to_scan)

start_time = get_start(data_start)

print("Start time is: {}".format(start_time))

time, temperature, pressure, rel_hum = get_data(the_file, start_time)

if len(time) < 3:
    print("Please check starting times\nProgram Exiting")
    quit()

# With data, create save path and title to give the functions
save_path = "{}.png".format(the_file.split('.')[0])
title = 'Sensor Data: {}'.format(the_file.split('.')[0].split('/')[2])

fig = plt.figure()  # This is the 'canvas' of the plot. Used later for changes

ax1 = plt.subplot(1, 1, 1)
ax1.plot(plot_times, plot_variable, label='Official Data')
ax1.plot(time, temperature, label='unofficial data')

# this is what make the x-axis format correctly
xfmt = mdate.DateFormatter('%H:%M')
ax1.xaxis.set_major_formatter(xfmt)
fig.autofmt_xdate()

plt.title('Homemade vs Official Data Comparison')
plt.ylabel('Temperature')
plt.xlabel('Time (Hour:Minutes)')

plt.legend()
plt.show()
