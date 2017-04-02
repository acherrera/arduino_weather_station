"""
This is a script that will plot ASOS data vs recorded data.
ASOS data file goes under "official_file"
Recorded data goes under "unofficial_file"
"""

import tkinter as tk
from tkinter import filedialog

import datetime
import matplotlib.dates as mdate
import matplotlib.pyplot as plt

from modules.functions import get_start, get_data, data_start


# ===================== ASOS file handling =========================

input("Next Screen is the official file input - any key to continue")

# This file has to be downloaded as a CSV file to work
# File location from user using pretty GUI
root = tk.Tk()                      # make it
root.withdraw()                     # how to
raw_path = filedialog.askopenfile() # what to
root.destroy()                      # get rid of

# This is needed to make the file path work correctly
official_file = raw_path.name

# Opens file and gets data out of it
with open(official_file) as f:
    data = f.readlines()

# 'Cleans' the data to remove comments and other information
raw_data = []
for line in data:
    # Take out tops line if they are not a comment or blank
    if line.startswith('#') or line == '\n':
        pass
    else:
        raw_data.append(line)

# Top line is just a header - remove it and save it reference if needed
header = raw_data.pop(0)

print(header)

# Defining emptys lists to be used later to add data
station = []
time = []
temperature = []
dew_point = []
rel_hum = []
dirct = []

times = []


# Quick function that inserts None if data is missing - lots of missing data in files.
# Actually does nothing but thought it might make graphing work better later - it doesn't
def data_adder(item, parent_list):
    if item == 'M':
        parent_list.append(None)
    else:
        parent_list.append(item)


# For each line, add the variables to the appropriate list
for line in raw_data:
    sample = line.split(',')  # Turns into list - makes the parsing messy because of indexing

    data_adder(sample[0], station)
    time = sample[1]  # this is indexing odd.
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

# Because of all missing data, have to remove missing data before plotting. Could leave missing data
# as 'M' but already have it replaced with None type, so I'm leaving it for now
plot_times = []
plot_variable = []

# runs through the list by index rather than actual value so when it comes back with a value, both the value
# and associated time can be added to the list
for i in range(len(temperature)):
    if temperature[i] is not None:
        plot_variable.append((float(temperature[i]) - 32) / 1.8)
        plot_times.append(times[i])



# ================= Unofficial File Handling ==================

input("Next Screen is the unofficial file input - any key to continue")

# This file has to be downloaded as a CSV file to work
# File location from user using pretty GUI
root = tk.Tk()                      # make it
root.withdraw()                     # how to
raw_path = filedialog.askopenfile() # what to
root.destroy()                      # get rid of

# This is needed to make the file path work correctly
unofficial_file = raw_path.name

lines_to_scan = 40  # lines to scan for the first non-comment line

data_start = data_start(unofficial_file, lines_to_scan)

start_time = get_start(data_start)

print("Start time is: {}".format(start_time))

time, temperature, pressure, rel_hum = get_data(unofficial_file, start_time)


# With data, create save path and title to give the functions
save_path = "{}_comparison.png".format(unofficial_file.split('.')[0])
title = 'Sensor Data: {}'.format(unofficial_file.split('.')[0].split('/')[2])

fig = plt.figure()  # This is the 'canvas' of the plot. Used later for changes

# Actually plotting the data - with labels and everything
ax1 = plt.subplot(1, 1, 1)
ax1.plot(plot_times, plot_variable, label='Official Data')
ax1.plot(time, temperature, label='unofficial data')

# this is what make the x-axis format correctly
xfmt = mdate.DateFormatter('%H:%M')
ax1.xaxis.set_major_formatter(xfmt)
fig.autofmt_xdate()

plt.title('Homemade vs Official Data Comparison')
plt.ylabel('Temperature(C)')
plt.xlabel('Time (Hour:Minutes)')

plt.legend()
plt.savefig(save_path)
plt.show()
